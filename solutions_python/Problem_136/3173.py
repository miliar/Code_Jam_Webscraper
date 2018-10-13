C,F,X,B=None,None,None, 2.0
import sys

def main():
    global C,F,X
    f = 'cookies.sample.in'
    f = sys.argv[1]
    f = open(f)
    N = int(f.readline())
    for i in xrange(N):
        l = f.readline().strip().split()
        C,F,X = map(float, l)
        print 'Case #%d:'%(1+i), solve()

def solve():
    a,b = 0, (int(X/C)+1)
    fa, fb = map(f, (a,b))

    while 1:
        if (b-a) <= 1:
            break
        
        m = int((a+b)/2.0)
        fm = f(m)
        fmp = f(m+1)

        if fmp>fm:
            b = m
        else:
            a = m

    return min(f(a), f(b))
        
def f(n):
    t = (C / (B + i*F) for i in xrange(n))
    t = sum(t)
    
    mr = B + n*F
    return t + X/mr


main()
