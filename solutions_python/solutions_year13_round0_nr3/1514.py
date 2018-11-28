#!/usr/bin/env python2


def is_fair(pal) :
    return (pal == pal[::-1])

def intsqrt(n):
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y

def intsqrspal(lower, upper) :
    vmin = intsqrt(lower)
    if (vmin*vmin < lower) :
        vmin += 1
    vmax = intsqrt(upper)
    value = vmin
    while value <= vmax :
        if is_fair(`value`) :
            yield value*value
        value += 1


# GENERATE THE RESULT LIST
RESULTLIST = []
for value in intsqrspal(1,pow(10,14)) :
    if is_fair(`value`) :
        RESULTLIST.append(value)

# RUN
for t in xrange(1,int(raw_input())+1) :
    vmin_s,vmax_s = raw_input().split()
    vmin,vmax = int(vmin_s),int(vmax_s)
    count = 0
    for value in RESULTLIST :
        if value >= vmin and value <= vmax :
            count += 1
    print "Case #" + `t` + ": " + `count`
