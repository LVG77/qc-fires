from typing import Dict
import json
import urllib.request
import urllib.parse

def get_json()->Dict:
    url = 'https://sopfeu.qc.ca/wp-admin/admin-ajax.php'
    data = {
        'type': 'activites',
        'zone': 1,
        'action': 'wplr_push_popup_stats',
        'nonce': '738609c2ce',
    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as r:
        jdata = json.loads(r.read().decode())
    return jdata

if __name__ == "__main__":
    res = get_json()
    open('feux.json', 'w').write(json.dumps(res['data']['obj'], indent=4, ensure_ascii=False))