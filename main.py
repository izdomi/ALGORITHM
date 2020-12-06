import random
from random import randrange
import math

def find_squeare(x):
    g = random.choice(range(1 ,x))
    while g *g != x:
        g = (g + x / g) / 2
        if x == g * g:
            return g

print(find_squeare(16))

def findSqrt(nr):
    g = round(nr/ randrange(1,nr))
    while nr!= g*g:
        print(g*g, (g+nr/g)/2)
        if (nr==math.ceil(g*g)):
            return g
        else:
            g = (g+nr/g)/2

print(findSqrt(8))


def convert_binary(n):
    if n >= 0:
        d = n
        binary = ""
    while d != 0:
        r = d % 2
        if (r == 1):
            binary = "1" + binary
        else:
            binary = "0" + binary
        d = (d-r)/2
        return binary
    else:
        return 0
print(convert_binary(20))

def gcd(a,b):
    while a != b:
        if a > b:
            a = a - b

        else:
            b = b - a

    else:
        return a

print(gcd(144,12))
