
def d(C, F, X, n):
    t = 0
    for i in range(n):
        x = 1.0*C/(2+i*F)
        t += x
    return t + 1.0*X/(2+n*F)

def solve(C, F, X):
    i = 0
    while 1:
        a = d(C,F,X,i)
        b = d(C,F,X,i+1)
        if b>=a:
            return a
        i += 1


def p(fn):
    f = open(fn)
    T = int(f.next())
    for i in range(T):
        C, F, X = map(float, f.next().split())
        print 'Case #%s: %s' % (i+1, solve(C, F, X))

if __name__ == '__main__':
    p('B-small-attempt1.in')
    #print solve(1.00382, 3.42909, 100.83592)
    #print solve(30.0, 1.0, 2.0)
    #print solve(30.0,2.0,100.0)
    #print solve(30.50000,3.14159,1999.19990)
    #print solve(500.0,4.0,2000.0)

