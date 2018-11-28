import sys

def foo3(a):
    b = []
    for x in a:
        for j in range(len(x)+1):
            b.append(x[:j])
    #print set(b)
    return len(set(b))



def foo2(a, x):
    res = 0
    for y in x:
        res += foo3([a[i] for i in y])
    return res

def enum(m, n):
    if m == 0:
        yield [[] for i in range(n)]
        return
    for x in enum(m-1, n):
        for i in range(n):
            x2 = x[:]
            x2[i] = x2[i]+[m-1]
            yield x2

def enum2(m, n):
    for x in enum(m, n):
        ok = True
        for y in x:
            if len(y) == 0:
                ok = False
                break
        if ok:
            yield x

def foo(ifile):
    m, n = [int(x) for x in ifile.readline().split()]
    a = [ifile.readline().strip() for i in range(m)]
    res = 0
    resc = 0
    for x in enum2(m, n):
        t = foo2(a, x)
        #print x , t
        if t > res:
            res = t
            resc = 1
        elif t == res:
            resc += 1
    return "%s %s" % (res, resc)

def main(ifile):
    n = int(ifile.readline().strip())
    for i in range(n):
        print 'Case #%s: %s' % (i+1, foo(ifile))

main(sys.stdin)

