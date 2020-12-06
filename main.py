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