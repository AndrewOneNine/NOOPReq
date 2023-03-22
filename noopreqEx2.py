import requests
import os

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        return headers

    def get_file_list(self):
        url_to_upload = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        resp = requests.get(url_to_upload, headers=self.get_headers())
        resp_json = resp.json()
        return resp_json

    def get_upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {
            'path': file_path,
            'overwrite': 'true'
        }
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        href = data.get('href')
        #print(href)
        return href

    def upload(self, file_path, file_name):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        href = self.get_upload_link(file_path=file_path)
        response = requests.put(href, data=open(file_name, 'rb'))
        if response.status_code == 201:
            print('Success')
        #print(resp.json())
        return response.json()


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file_v_name = input('Введите путь к файлу с его наименованием: ')
    path_to_file = os.path.basename(path_to_file_v_name)
    token = input('Введите свой токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, path_to_file_v_name)