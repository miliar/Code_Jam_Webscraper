from sys import stdin, stdout
from math import ceil, sqrt
from decimal import *
lines = stdin.read().split('\n')
ntests = int(lines.pop(0))

for test in range(ntests):
    stdout.write("Case #"+str(test+1)+": ")
    getcontext().prec = 100
    r,t = map(Decimal,map(int,lines[test].split(' ')))

    x = Decimal((-3 - 2*r + (1 + 8*t - 4*r + 4*r*r).sqrt())/4)
    if not x%1: x+=1 
    stdout.write(str(int(ceil(x)))+'\n')