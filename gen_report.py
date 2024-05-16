import requests
import os 
from sys import argv

url = 'http://localhost:8000/api/gen_report/'

with open(argv[1], 'rb') as img:
    name_img = os.path.basename(argv[1])
    files = {'image': img}
    requests.post(url,data={
        'task_id': int(input('Введите номер задачи: ')), 'model_id': int(input('Введите id модели: '))
        },files=files)

