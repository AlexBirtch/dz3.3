import requests
from urllib.parse import urlencode
from data import *

# APP_ID = APP_ID
AUTH_URL = 'https://oauth.vk.com/authorize'


aut_data = {
    'client_id': APP_ID,
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.92'
}

print('?'.join((AUTH_URL, urlencode(aut_data))))


class UserVk:
    # TOKEN = TOKEN
    vk_link = 'https://api.vk.com/method/'
    param = {'v': '5.92',
             'access_token': TOKEN}

    @staticmethod
    def get_response(request_link, method):
        return requests.get(f'{request_link}{method}', UserVk.param).json()

    def __init__(self, user_id):
        self.user_id = user_id
        self.link = f'https://vk.com/id{self.user_id}'

    def __and__(self, other):
        UserVk.param['source_uid'] = self.user_id
        UserVk.param['target_uid'] = other.user_id
        method = 'friends.getMutual'
        return list(map(UserVk, UserVk.get_response(UserVk.vk_link, method)['response']))

    def __repr__(self):
        return f'{self.user_id}'

    def __str__(self):
        return f'{self.user_link}'

    def get_user_link(self):
        return self.link

    user_link = property(get_user_link)


if __name__ == "__main__":
    user_input = input('введите два id номера через пробел для поиска общих друзей: ').split()
    user1 = UserVk(user_input[0])
    user2 = UserVk(user_input[1])

    print(user1 & user2)


    print(f'Для пользователей: {user1.user_id} & {user2.user_id} ' )
    print('найдены общие друзья:')
    for item in user2 & user1:
        print(item)
    print(f'\nссылка на пользователя №1: {user1}')
    print(f'ссылка на пользователя №2: {user2}')