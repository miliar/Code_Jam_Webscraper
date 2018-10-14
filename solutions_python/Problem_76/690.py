import sys
import itertools

def xor(values, indices):
    result = 0
    for index in indices:
        result ^= values[index]
    return result

f = open(sys.argv[1],'r')
t = int(f.readline())
for i in xrange(t):
    n = int(f.readline())
    c = map(int,f.readline().split())
    currentMax = -1
    indices = [x for x in xrange(len(c))]
    p = [0]
    others = set(indices) - set(p)
    value1 = xor(c, others)
    value2 = c[0]
    if value1 == value2:
        c.sort()
        currentMax = sum(c[1:])
    if currentMax == -1:
        currentMax = "NO"
    else:
        currentMax = str(currentMax)
    print "Case #%d: %s" % (i+1, currentMax)