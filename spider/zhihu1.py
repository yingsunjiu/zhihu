
import random,time
import requests
from bs4 import BeautifulSoup

INDEX_URL = 'http://www.zhihu.com'
LOGIN_URL = 'http://www.zhihu.com/login/email'
CAPTCHA_URL = 'http://www.zhihu.com/captcha.gif?r='

def gen_time_stamp():
    return str(int(time.time())) + '%03d' % random.randint(0, 999)

def login(username, password):
    session = requests.session()

    _xsrf = BeautifulSoup(session.get(INDEX_URL).content).find('input', attrs={'name': '_xsrf'})['value']
    data = {
        '_xsrf': _xsrf,
        'email': username,
        'password': password,
        'remember_me': 'true',
    }
    response = session.post(LOGIN_URL, data)
    if response.getcode() != 200:
        raise Exception('captcha error.')
    print response.read()
    return session



if __name__ == "__main__":
    login("zhixiangchai@163.com","czx88888")
