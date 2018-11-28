#import time

ten = [1, 10, 100, 1000, 10000, 100000, 1000000]
lut = {}

def foo(a, b):
    astr = str(a)
    l = len(astr)
    res = 0

    for i in xrange(a, b):
        klst = []
        for j in xrange(1, l):
            tenj = ten[j]
            k = i % tenj *  ten[l - j] + i / tenj
            
            if k <= b and i < k and k not in klst :
                #print i, "  ", int(tstr[l-j:]) * 10 ** (l-j) + int(tstr[:l-j]),
                klst.append(k)
                res += 1
        if klst:
            klst.sort()
            lut[i] = klst

    #return (a,b), res
    return res

def countit(a,b):
    count = 0 
    for i in xrange(a, b):
        for j in lut.get(i, []):
            if j <= b:
                count += 1
            elif j>b:
                break
    return count


def init():
    foo(1      , 9)
    foo(10     , 99)
    foo(100    , 999)
    foo(1000   , 9999)
    foo(10000  , 99999)
    foo(100000 , 999999)
    foo(1000000, 2000000)
    
def doit():
    init()
    t = int(raw_input())
    for i in xrange(t):
        a,b = map(int, raw_input().split())
        print "Case #%s: %s" %(i+1, countit(a,b))

doit()

"""
def f(a, b):
    t1 = time.time()
    res = countit(a,b)
    t2 = time.time()
    print " %7d\t%7d\t\t%s\t" % (a,b, res), "Time taken : ", t2 - t1

def test_init():
    t1 = time.time()
    print foo(1      , 9)
    print foo(10     , 99)
    print foo(100    , 999)
    print foo(1000   , 9999)
    print foo(10000  , 99999)
    print foo(100000 , 999999)
    print foo(1000000, 2000000)
    t2 = time.time()

    print "Time taken to initialize : %s" % (t2 - t1)
    print "length %s \n" % len(lut)


def test():
    test_init()
    f(1,9)
    f(10,40)
    f(100,500)
    f(1111, 2222)
    f(100000 , 999999)
    f(1000000, 2000000)
    t1 = time.time()
    for i in xrange(100):
        foo2(1000000, 2000000)
    t2 = time.time()
    print "Time taken : %s" % (t2 - t1)

test()
"""

