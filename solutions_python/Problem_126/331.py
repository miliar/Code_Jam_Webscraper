#/usr/bin/cython --embed -2 A.pyx
#/usr/bin/gcc -o A -I/usr/include/python2.7 A.c /usr/lib/libpython2.7.so
#./A

import sys

def q():
    s, n = sys.stdin.readline().split()
    n = int(n)
    P = []
    c = 0
    k = 0
    for i in range(len(s)):
        if s[i] in 'aeiou':
            c = 0
        else:
            c += 1
            if c>=n:
                P.append(i-n+1)
                
    
    #sys.stderr.write('%s\n' % P)
    
    ans = 0
    for k in range(len(P)):
        for i in range(len(P) - k): # i .. i+k+1
            l = P[i] + 1
            if i>0: l = P[i] - P[i-1]
            r = len(s) - P[i+k] - n + 1
            if i+k<len(P)-1: r = P[i+k+1] - P[i+k]
            ans += l*r
            #sys.stderr.write('%d %d %d %d\n' % (k, i, l, r))
    return ans

T = int(sys.stdin.readline())
for t in range(T):
    print 'Case #%d: %d' % (t+1, q())
    