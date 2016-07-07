
from urllib import urlretrieve

import getpass
import os
import vk

APPLICATION_ID = '5538517'
login = input('Enter your login: ')
password = getpass.getpass('Enter your password: ')
session = vk.AuthSession(app_id=APPLICATION_ID,
                         user_login=login,
                         user_password=password,
                         scope='audio')
api = vk.API(session, v='5.52', lang='en')
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
