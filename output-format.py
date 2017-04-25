#!/usr/bin/python3.5

username = input("name:")
yourage = int(input("age:"))
job = input("yourjob:")

info1 = '''****  info of %s ***
name:%s
age:%d
job:%s

''' %(username,username,yourage,job)

print (info1)

print('--------------------------------')
username = input("name:")
yourage = int(input("age:"))
job = input("yourjob:")

info2 = '''****  info of {Name} ***
name:{Name}
age:{Age}
job:{Job}

''' .format(Name=username,Age=yourage,Job=job)


print (info2)

