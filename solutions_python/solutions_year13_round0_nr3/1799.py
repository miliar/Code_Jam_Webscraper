#!/usr/bin/env python

from numpy import *

def inputs():
    return tuple(map(long, raw_input().split(' ')))

tabc = 0

def sqrt(x):
    if x < 100:
        return long(math.sqrt(x))
    global tabc
    tabc += 1
    sx = str(x)
    if len(sx) % 2 == 1:
        sx = '0' + sx
    q = 0L
    l = 0L
    r = 0L
    for i in range(0, len(sx), 2):
        s = r*100 + long(sx[i:(i+2)])
        for temp in reversed(range(10)):
            if (20*q + temp)*temp <= s:
                break
        q = 10*q + temp
        r = s - temp**2
        #for i in range(tabc):
        #    print ' ',
        #print s, temp, q, r
    tabc -= 1
    return q

(T,) = inputs()
for t in range(T):
    print "Case #%d:" % (t+1,),
    (A, B) = inputs()
    
    a = sqrt(A)
    if a**2 < A:
        a += 1
    assert(a**2 >= A)
    sa = str(a)
    na = len(sa)
    if long(sa[:(na+1)/2] + sa[:na/2][::-1]) >= a:
        pa = long(sa[:(na+1)/2])
    else:
        pa = long(sa[:(na+1)/2])+1
    
    b = sqrt(B)
    assert(b**2 <= B)
    sb = str(b)
    nb = len(sb)
    if long(sb[:(nb+1)/2] + sb[:nb/2][::-1]) <= b:
        pb = long(sb[:(nb+1)/2])
    else:
        pb = long(sb[:(nb+1)/2])-1
    
    def count(x):
        result = 0
        ix1 = 0L
        ix2 = 0L
        for x_i in x:
            ix1 = ix1*10 + x_i
            ix2 = ix2*10 + x_i
        ix2 = ix2*10 + x[-1]
        for x_i in reversed(x[:-1]):
            ix1 = ix1*10 + x_i
            ix2 = ix2*10 + x_i
        if ix1 > b:
            return 0
        k = len(x)
        s = 9
        for i in range(1, k):
            s -= x[i]*x[k-i]
        max_x_k = s/x[0]
        if a <= ix1 and ix1 <= b:
            result += 1
        if a <= ix2 and ix2 <= b:
            result += 1
        for x_k in range(max_x_k + 1):
            result += count(x + [x_k])
        return result
    
    print count([1]) + count([2]) + count([3])
