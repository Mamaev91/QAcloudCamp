import requests
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

def get_title():
    """Получаем данные в формате json"""
    response = requests.get(url=data["url"])
    r = response.json()
    title = [i["title"] for i in r]
    return title

def create_post():
    """Создаем новый пост"""
    response = requests.post(url=data["url"], data={"userId": data["userId"],
                                                    "id": data["id"],
                                                    "title": data["title"],
                                                    "body": data["body"]})
    return response.status_code

def delete():
    """Удаляем пост"""
    response = requests.delete(url="https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

