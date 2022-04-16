import requests


def get_repos():
    url = "https://api.github.com/users/stackbuilders/repos"
    data = requests.get(url)
    return data.json()
