import math
import string

def gcd(a, b):
    if b != 0:
        return gcd(b, a%b)
    return a
    
def doit(L):
    mcd = abs(L[0] - L[1])
    for i in range(0, len(L)):
       for j in range(i+1, len(L)):
          mcd = gcd(mcd, abs(L[i] - L[j]))
    ret = 0
    for i in range(0, len(L)):
       val = mcd - L[i] % mcd
       if (val == mcd):
           val = 0
       ret = max(ret, val)
    return ret

N = int(input())
for i in range(1, N + 1) :
    x = string.split(raw_input())
    print 'Case #' + str(i) + ':', doit([long(x[i]) for i in range(1, int(x[0]) + 1)])

