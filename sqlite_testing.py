import sqlite3

#
# conn = sqlite3.connect('Hizer_demo.db')
#
# c = conn.cursor()
# #
# c.execute("""CREATE TABLE hizer (
#             name text,
#             password text,
#             Facebook text,
#             Instagram text,
#             Telegram Text,
#             Email text,
#             Phone_number text,
#             Git text,
#             LinkedIn text
#             )""")
# #
# conn.commit()
# conn.close()

username = input('USERNAME: ')
password = input('PASSWORD: ')

# facebook = input('FACEBOOK: ')
# instagram = input('INSTAGRAM: ')
# git = input('GIT: ')
# telegram = input('TELEGRAM: ')
# mail = input('MAIL: ')
# phone = input('PHONE: ')
# linkedin = input('LINKEIN: ')
# res = []
#
# for el in [username, password, facebook, instagram, git, telegram, mail, phone, linkedin]:
#     if el == '':
#         print('yaaaas')
#         el = 'NULL'
#         print(el)
#     else:
#         print('NAAAH')
#
#     res.append((el))

# with sqlite3.connect('Hizer_demo.db') as data_base:
#     cursor = data_base.cursor()
#
#     find = """INSERT INTO hizer (name, password, Facebook, Instagram, Telegram,
#     Email, Phone_number, Git, LinkedIn) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
#
#     cursor.execute(find, res)
#
#     # print([(username), (password), (facebook), (instagram),
#                           # (telegram), (mail), (phone), (git), (linkedin)])
#     data_base.commit()
#

# with sqlite3.connect('Hizer_demo.db') as data_base:
#     cursor = data_base.cursor()
#
#     check_user = "SELECT ? FROM hizer WHERE ? IN (SELECT name FROM hizer)"
#
#     cursor.execute(check_user, [(username), (username)])
#
#     result = cursor.fetchall()
# print(result)




# CHECK_PASSWORD
# with sqlite3.connect('Hizer_demo.db') as data_base:
#     cursor = data_base.cursor()
#
#     check_password = "SELECT name FROM hizer WHERE password = ?"
#
#     cursor.execute(check_password, [(password)])
#
#     result = cursor.fetchall()
#
#     for tpl_user in result:
#         if tpl_user == (username,):
#             print('1')
#         else:
#             print('0')

