from typing import Dict
import re
import json
import urllib.request
import urllib.parse

def get_json()->Dict:
    url = 'https://sopfeu.qc.ca/wp-admin/admin-ajax.php'
    url_main = 'https://sopfeu.qc.ca/'

    req_main = urllib.request.Request(url_main, method='GET')
    with urllib.request.urlopen(req_main) as r:
        html = r.read().decode('utf-8')
    start_re = re.compile(r'ajaxNonce":')
    end = ',"adminAjax"'
    new_nonce = start_re.split(html)[1].split(end)[0].strip('\"')

    data = {
        'type': 'activites',
        'zone': 1,
        'action': 'wplr_push_popup_stats',
        'nonce': new_nonce,
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as r:
        jdata = json.loads(r.read().decode())
    return jdata

if __name__ == "__main__":
    res = get_json()
    open('feux.json', 'w').write(json.dumps(res['data']['obj'], indent=4, ensure_ascii=False))