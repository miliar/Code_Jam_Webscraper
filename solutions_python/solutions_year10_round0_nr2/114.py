import sys
import math

def gcd(x, y):
    if y==0:
        return x
    return gcd(y, x%y)

def solve(N, ti):
    g = abs(ti[1] - ti[0])
    for t in ti[2:]:
        g = gcd(g, abs(t-ti[0]))
    return (-ti[0])%g

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    N = int(line[0])
    ti = [int(line[i+1]) for i in range(N)]
    res = solve(N, ti)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
