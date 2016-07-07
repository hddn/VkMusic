
from urllib import urlretrieve

import getpass
import os
import vk

# Id for our VK application
VK_APPLICATION_ID = '5538517'

# VK API version
API_VERSION = '5.52'

login = input('Enter your login: ')
password = getpass.getpass('Enter your password: ')
session = vk.AuthSession(app_id=VK_APPLICATION_ID,
                         user_login=login,
                         user_password=password,
                         scope='audio')
api = vk.API(session, v=API_VERSION, lang='en')
files = api.audio.get()
files_count = files['count']
root = os.path.realpath(os.path.dirname(__file__))
path = os.path.join(root, "downloads")

if not os.path.exists(path):
    os.makedirs(path)

print('Need to download {} tracks'.format(files_count))

for file in files['items']:
    url = file['url']
    print('Downloading {} - {}'.format(file['artist'], file['title']))
    urlretrieve(url, path + '/' + file['artist'] + ' - ' + file['title'])
print('Download complete.')
