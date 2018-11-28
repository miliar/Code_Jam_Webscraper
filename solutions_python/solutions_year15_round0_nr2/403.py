import random

T = int(raw_input())

for index in xrange(T):
    raw_input()
    p = map(int, raw_input().split(' '))
    pmax = max(p)
    a, minimum = 0, pmax
    record = (0, pmax)
    for b in xrange(2, pmax):
        a = 0
        for p_i in p:
            if p_i % b == 0:
                a = a + max(0, p_i / b - 1)
            else:
                a = a + max(0, p_i / b)
        #print a,b
        if a + b < minimum:
            minimum = a+b
            record = (a, b)
    #print record
    result = str(minimum)
    print "Case #%d: " % (index+1) + result

