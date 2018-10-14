from math import *

def toint(x, odd):
    last = -1 if odd else len(x)
    xx = x[:] + list(reversed(x[:last]))
    r = sum(x * 10**i for i, x in enumerate(xx))
#    print xx, r
    return r

def count_d(nd, a, b):
    n = 0
    nd = int(floor(nd / 2.0))
    x = []
    x.append(1)
    for _ in xrange(1, nd):
        x.append(0)
    while True:
        for odd in xrange(2):
            y = toint(x, odd)
            yy = y**2
            if yy < a:
                continue
            if yy > b:
                continue
            if ispal(yy):
                n += 1
        carry = 0
        x[len(x)-1] += 1
        for j in xrange(len(x)-1, -1, -1):
            x[j] += carry
            if x[j] == 4:
                x[j] = 0
                carry = 1
            else:
                carry = 0
        if carry == 1:
            break
    return n

def ispal(n):
    n = str(n)
    l = len(n)
    for i in xrange(l/2):
        if n[i] != n[l-i-1]:
            return 0
    return 1

def compute2(A, B):
    n = 0
    a = int(ceil(sqrt(A)))
    b = int(floor(sqrt(B)))
    la = len(str(a))
    lb = len(str(b))
    la += la % 2
    lb += lb % 2
    for i in xrange(la, lb + 1, 2):
        n += count_d(i, A, B)
    print '%d' % n

def compute(A, B):
    n = 0
    for i in xrange(int(ceil(sqrt(A))), int(floor(sqrt(B))) + 1):
        sqr = i**2
        if not ispal(i):
            continue
        if not ispal(sqr):
            continue
        n += 1
    print '%d' % n

def run():
    T = int(raw_input())
    for i in xrange(T):
        A, B = [int(x) for x in raw_input().split()]
        print 'Case #%d:' % (i + 1),
#        compute(A, B)
        compute2(A, B)

if __name__ == '__main__':
    run()
#    count_d(6, 0, 1e9)
