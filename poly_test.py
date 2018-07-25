from polynomial import *


p = 47

z = 5

for x in range(p):
    print(x, (z**x) % p)