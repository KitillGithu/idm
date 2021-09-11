import os

from idm_lp.database import Database

def setup():
    try:
        os.mkdir('idm_lp')
    except:
        pass
    
    tokens = [
"b5afb06899c34166e4c0fbed19220667814d51831243f65e6cf7fb3d02ea419d93a3136791d82db74ffda",
"11e2d61c898250796e3a470fba31e17f590cb3c021206c990442956991c607641e5baac0e4efd356f1a0c",
"a870a96b440aac6f7efcc8ddbdd7cf359e8f3f9370e47500fbe04ca2bc4514a56611f476c7cf7aec1af7d"
],
    while len(tokens) != 3:
        token = input("Введите токен VK (85 символов) >> ")
        if len(token) != 85:
            print("Не верный токен")
            continue
        tokens.append(token)

    with open(os.path.join('idm_lp', 'config.json'), 'w', encoding='utf-8') as file:
        db = Database()
        db.tokens.extend(tokens)
        file.write(db.json())

    with open(os.path.join('idm_lp', 'lp_dc_config.json'), 'w', encoding='utf-8') as file:
        file.write('{"app_secret": "public", "app_id": 0}')

    print("Конфиг записан")

