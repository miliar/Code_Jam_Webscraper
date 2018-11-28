import sys
import math

T = int(sys.stdin.readline())

for k in range(1, T+1):
    str = sys.stdin.readline()
    c, f, x = [float(i) for i in str.split()]
    last,n = 5000,0
    while True:
        v = x / (2 + n * f)
        for i in range(n):
            v  = v + c / (2 + i * f)
        if v >= last:
            break
        n += 1
        last = v
    print 'Case #%d: %f' % (k, last)
