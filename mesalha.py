

#helloooo
import calendar
y = int(input('enter year:'))
m = int(input('enter month:'))
print(calendar.month(y,m))

from datetime import date
f_date = date(2024,1,1)
l_date = date(2024,5,13)
delta = l_date - f_date
print(delta)

import getpass
print(getpass.getuser())

import socket
print(socket.gethostbyname(socket.gethostname()))
'''

'''
while True:
    try:
        a = int(input('enter a number:'))
        break
    except ValueError:
        print('\n this is not a number. try again...')
        print()
'''
'''
import socket
addr =input('enter ip address:')
try:
    socket.inet_aton(addr)
    print('valid IP')
except socket.error:
    print('invalid IP')
'''
'''
import math
class Circle:
    def __init__(self,r) :
        self.redius = r

    def masahat(self):
        return self.redius **2 * math.pi
    def mohit(self):
        return self.redius * 2 *math.pi

newcircle = Circle(5)
print(Circle.masahat(newcircle))
print(Circle.mohit(newcircle))
'''

import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com' , 'nabeghaha.com/shop'])
    webbrowser.open(sites)
    second = random.randrange(5,20)
    time.sleep(second)