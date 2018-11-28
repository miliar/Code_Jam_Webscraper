import sys

def flip(i):
    a = str(i)
    ans = ''
    for i in xrange(len(a)):
        ans += a[len(a) - 1 - i]

    return int(ans)

def solve(N):
    if N < 11:
        return N
    
    x = [0]*(N+1)
    x[1] = 1
    x[2] = 2

    for i in xrange(3,len(x)):
        if flip(i) < i and len(str(flip(i))) == len(str(i)):
            x[i] = min(x[i-1] + 1, x[flip(i)] + 1)
        else:
            x[i] = x[i-1] + 1

    return x[N]


# Run this first!!
"""
f = open('Cache.txt','w')
f.write(str(solve(1000001)))
f.close()
"""


"""
f = open('Cache.txt','r')
a = f.read()
x = eval(a)
f.close()
"""

T = int(sys.stdin.readline())
for case in xrange(T):
    N = int(sys.stdin.readline())
    print 'Case #%d: ' % (case + 1) + str(solve(N))
    
