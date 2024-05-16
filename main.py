import requests
import datetime

url = 'http://localhost:8000/api/post_workday/' 
response = requests.post(url, data={'empl_id': int(input('Id работника: ')), 'date': str(datetime.datetime.now().date())}) 
response_on_python = response.json()
if response.status_code == 200:
    print('OK')
elif response.status_code == 400:
    print(f'Error: {response_on_python['errors']}')
