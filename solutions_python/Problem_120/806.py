from math import *
from decimal import *
getcontext().prec = 100
d = Decimal
def main():
    count = int(raw_input())
    for i in range(count):
        l = raw_input()
        r = d(l.split(' ')[0])
        t = d(l.split(' ')[1])
        n = (int(sqrt((2*r-1)**2+8*t))-2*int(r)+1)/4
        print 'Case #'+str(i+1)+': '+str(n)
main()
