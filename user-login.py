#!/usr/bin/env python
#该代码是实现用户登录成功是显示登录成功，当账号信息错误时有3次尝试的机会，超过3次则账号被锁定
import getpass

Username = "admin"
Password = "adminpwd"


locklist = ["jack","lilei"]
namelist = open('locklist.txt').read()
#namelist = filename.readline()

count = 0
while count < 3:
	username = input("username:").strip()
	password = getpass.getpass("password:").strip()
	if username in namelist:
		print("I'm sorry,your account have locked,please connecation your administrator.")
		break
	if username == Username and password == Password:
		print("Welcome user {name} login this system......".format(name=username))
		break
	else:
		print("invalid username or password......")
		#continue
	count += 1
else:
	#locklist.append(username)
	print("you have tried three times,your account have locked.")
	#print(locklist)
	with open('locklist.txt','a+') as f:
		f.write(username +'\n')
