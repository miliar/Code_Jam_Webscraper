from numpy import *

f = open('2.txt', 'r')
n = int(f.readline())

def t(n, X, C, F):
    if n<=0: return X/2.0
    else:
        return sum(C/(2+arange(n)*F)) + X/(2.+n*F)

for i in range(n):
    C, F, X = map(float, f.readline().split(' '))
    n = int(round(X/C - 2.0/F - 1))
    t1 = t(n-1, X, C, F)
    t2 = t(n, X, C, F)
    t3 = t(n+1, X, C, F)

    if t1 <= t2 and t1<= t3: ans = t1
    elif t2<= t1 and t2 <= t3: ans = t2
    else: ans = t3
    print "Case #{}: {:.7f}".format(i+1, ans)

f.close()
