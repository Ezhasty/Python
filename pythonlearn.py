l = ['Hello,', 'Sasha', 'Ezhasty'] 
l[0] = 'Hi' 

i = 0 
while i < 3: 
	print(l[i]) 
	i += 1 
	print(l[0:1:3]) 

a = tuple ("Sasha") 
print(a) 

b = (1, 3, 'Q', 'K', 'S', 'T', 1, 2, 3) 
print(b.count(3)) 

u = (1,3,6,9) 
print(u) 

c = (50, 100, 150, 200, 250, 'Hello') 
g = [1000, 2000, 3000, 4000, 5000, 'World!'] 
print(c) 
print(g) 
print (c.__sizeof__ ()) 
print (g.__sizeof__ ()) 

#Coded by Ezhasty 
#20.02.18 at 23:59
#Copyright()

d = {'name':{'name1':'1','name2':'Sasha','name3':'3'}} 
a = input('Введите имя:') 
if a == 'имя': 
	print('Ваше имя - ',d['name']['name2']) 
else: 
	print("Не правда!") 

a = input("Введите имя: ") 
if a == 'Vasya': 
	print("Yes, its a true!") 
else: 
	print("Its a false!") 

b = input("Введите фамилию: ") 
if b == 'Pupok': 
	print("Yes, of course!") 
else: 
	print("Its a false!") 
	print("Program was ended!") 

n = set ("Ezhasty") 
print(type(n)) 
print (n) 

newset = {'s', 'a', 'z', 'x', 'h', 'f', 'e',} 
newset.add('l') 
print(set(newset)) 
print(set(n)) 

print(n == newset) 

opa = 10098 
pop = 7889 
if opa > pop: 
	print(opa + pop) 
else: 
	print(opa - pop) 

newcort = (1, 's', 33, 543, 43) 
print(newcort.count(1)) 
print(newcort) 

newlist = [1, 3, 4, 6 ,7 ,8, 9] 
newlist.append(100) 
newlist[0] = 2 
print(newlist.sort()) 
print(newlist) 

d = {'key' : "Hello"} 
print(d) 
print("Хорошая работа ;D") 

dict0 = {'name' : 'Yopi'} 
dict1 = input("Введи своё имя!: ") 

if dict1 == dict0: 
	print("Круто!") 
else: 
	print(":d") 

print("Тутс-Тутс-Тутс") 

#Coded by Ezhasty 
#25.02.18 at 23:59
#Copyright()

def func (o, n):
	res = o * n
	return res

print(func(50, 100))

add = lambda x, y: x + y
print(add(2,3))

multiply = lambda f, s: f * s
print(multiply(3.4,3.34))

ol = 123
lol = 321

if ol < lol:
	print(add)
else:
	print(multiply)

def sum(u, i):
	return u + i

print(sum(30,45))

password = 'qwerty'
login = 'ezhasty'

m = input("Введите логин: ")

if m == login:
	print("Правда")
else:
	print("Не правда!")

j = input("Введите пароль: ")

if j == password:
	print("Правда")
else:
	print("Не правда!")

#Coded by Ezhasty 
#28.02.18 at 23:59
#Copyright()

try:
	num1 = 50
	num2 = 0
	print(num1 / num2)
	print("Выполнено")
except:
	print("Обнаружена ошибка, деление на ноль!")

try:
	k = int (input("Введите любое число, но не строку: "))
except ValueError:
	print("Вы ввели не число!")
	k = 0
else:
	print("Всё верно!")
finally:
	print("=D")

try:
	b = int (input("Введите любое второе число, но не строку: "))
except ValueError:
	print("Вы ввели не число!")
	b = 0
else:
	print("Всё верно!")
finally:
	print("=D")

k = int (input("Введите делимое: "))
b = int (input("Введите делитель: "))

try: 
	res = k / b
except ZeroDivisionError:
	print("Деление на ноль не возможно!")
	res = 0
print (res)

file = open ('python.txt')
print (file.read())
file.close()

with open('python2.txt', 'wt', encoding='utf-8') as inFile:
	numm = int(input("Введите число: "))
	line = str('1 / ' + str(numm) + ' = ' + str(1 / numm))
	print(line)
	inFile.write (line)

import time
import os
import random as r
from mymodule import hi as h, add as a
print (r.random())
h ()
print (a (13, 23))

class Person:
	name = "Петя, "
	age = 20

	def set(self, name, age):
		self.name = name
		self.age = age

sasha = Person ()
sasha.set ("Саша, ", 12) 
print(sasha.name + " " + str(sasha.age))

akakiy = Person ()
akakiy.set = ("Акакий, ", 23)
print (akakiy.name + " " + str(akakiy.age))

def decorator (func):
	def wrapper ():
		print("Код до выполнения функции")
		func()
		print("Код, после выполнения функции")
	return wrapper

@decorator
def show():
	print("Я обычная фунцкия")

show()

#Coded by Ezhasty 
#01.03.18 at 23:59
#Copyright()









