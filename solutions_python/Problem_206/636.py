import math, collections, copy, sys
f = open('input.in','r')
g = open('output.txt','w')
"""
just do it
"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    D, N = [int(x) for x in f.readline()[:-1].split(' ')]
    time = 0
    for i in xrange(N):
        K, S = [int(x) for x in f.readline()[:-1].split(' ')]
        time = max(time, 1.0*(D-K)/S)
    result = str("{:.7f}".format(D/time))
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()