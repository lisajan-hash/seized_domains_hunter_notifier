from helpers.requester import request_data
from datetime import datetime


key = "YOURAPI KEY"
api_version = "v1"
root_domain = "https://otx.alienvault.com/api"
hostnames = ["nsserver1", "nsserver2"]

headers = {
    'X-OTX-API-KEY': key,
    'User-Agent': "Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/57.2 Custom agent",
    'Content-Type': 'application/json'
}

def make_call():
    if len(hostnames) > 0:
        for nameserver in hostnames:
            hostname_domain = f"indicators/hostname/{nameserver}/passive_dns"
            url = f'{root_domain}/{api_version}/{hostname_domain}'
            a = request_data(method="GET", url=url, headers=headers)
            if a['success']:
                if len(a['result']['data']['passive_dns']) > 0:
                    for pdns in a['result']['data']['passive_dns']:
                        first_seen_str = pdns['first']
                        first_seen_date = datetime.fromisoformat(first_seen_str)
                        current_date = datetime.now()
                        days_difference = (current_date - first_seen_date).days
                        is_within_20_days = days_difference <= 20
                        if is_within_20_days:
                            print(f'URL {pdns['hostname']} had been less then 20 days ago , nameserver is {nameserver}')
                else:
                    print("server had not returned any result")
            else:
                print("Something went worng with your request")        
    else:
        print("No hostnames found in list")        


make_call()