import sys

sys.stdin = open('B.in')

t = int(raw_input())

def solve(n):
    n = list(n)
    i = len(n) - 1
    while i > 0:
        if int(n[i]) < int(n[i-1]):
            while i > 0 and int(n[i-1]) == 0:
                i -= 1
            n[i-1] = str(int(n[i-1]) - 1)
            for j in xrange(i, len(n)):
                n[j] = '9'
        i -= 1
            
    return int(''.join(n))

for i in xrange(t):
    n = raw_input()
    print 'Case #%d: %d' %(i+1, solve(n))
        