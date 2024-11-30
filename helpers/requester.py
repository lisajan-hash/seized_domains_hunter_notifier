import requests

def request_data(method, url, headers=None, params=None, data=None, json=None):
    try:
        response = requests.request(method, url, headers=headers, params=params, data=data, json=json)
        if response.status_code == 200 or response.status_code == 201:
            return {
                'success': True,
                'result': {
                    'status_code': response.status_code,
                    'data': response.json()
                }
            }
        else:
            # Handle other status codes
            return {
                'success': False,
                'result': {
                    'status_code': response.status_code,
                    'error': f'Error: Received status code {response.status_code}'
                }
            }
    except requests.HTTPError as http_err:
        return {
            'success': False,
            'result': {
                'status_code': response.status_code if response else None,
                'error': f'HTTP error occurred: {http_err}'
            }
        }
    except requests.RequestException as req_err:
        return {
            'success': False,
            'result': {
                'status_code': None,
                'error': f'Request error occurred: {req_err}'
            }
        }
    except Exception as err:
        return {
            'success': False,
            'result': {
                'status_code': None,
                'error': f'An unexpected error occurred: {err}'
            }
        }