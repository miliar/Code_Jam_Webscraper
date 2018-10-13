import operator
import sys
T = input()
for i in range(T):
    N = input()
    C = raw_input()
    C = C.split()
    C = [int(k) for k in C]
    x = 0
    for j in C:
        x = operator.xor(x,j)
    if x == 0:
        m = sum(C) - min(C)
        print "Case #%d: %d" % (i+1,m)
    else:
        print "Case #%d: NO" % (i+1,)
