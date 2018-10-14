# https://code.google.com/codejam/contest/2974486/dashboard#s=p1
import sys

def readline():
    return sys.stdin.readline().rstrip()

f0 = 2
t = int(readline())
for case in range(t):
    line = readline()
    [c, f, x] = [float(s) for s in line.split()]
    time = x/f0
    time2 = c/f0 + x/(f+f0)
    more = time2 < time
    factories = 0
    n = 0
    while more:
        factories = factories + c/(f*n+f0)
        time2 = factories + x/(f*(n+1)+f0)
        more = time2 < time
        time = min(time2, time)
        n = n+1
    result = time
    print 'Case #{}: {}'.format(case+1, result)
 

