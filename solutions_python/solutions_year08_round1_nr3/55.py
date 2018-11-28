
from math import log

def dofile(fname,outfname):
    result = dostr(file(fname).read())
    file(outfname,'w').write(result)

def dostr(s):
    dat = s.splitlines()

    #split to data sets
    T = int(dat[0])
    dat = dat[1:]
    results = []
    for i in xrange(T):
        n = int(dat[0])
        dat = dat[1:]
        results.append(solve(3,1,n,i+1))

    return '\n'.join(results)


def solve(A,B,n,ind):
    print A,B,n,ind
    (a,b) = s(A,B,n)
    b = q(5*b*b)
    res = (a+b) % 1000
    
    return "Case #%d: %03d" % (ind, res)
    

def s(A,B,n):
    if (n == 0):
        return (1,0)
    (a,b) = s(A*A+5*B*B, 2*A*B, n/2)
    if (n %2 == 0):
        return (a,b)
    else:
        return (A*a+5*B*b, B*a+A*b)

def q(y):
    bits = log(y,2)
    x=0
    for i in xrange(int(bits)+5,0,-1):
        xx = x+(1<<i)
        if xx*xx <= y:
            x = xx

    xx = x+1
    if xx*xx <= y:
        x = xx

    return x
    
