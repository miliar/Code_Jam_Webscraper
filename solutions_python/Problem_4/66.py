# using Py2.6
import sys
from itertools import izip, permutations

def proc(data1, data2):
    result = sys.maxint
    for perm1 in permutations(data1):
        res = sum(d1*d2 for d1,d2 in izip(perm1, data2))
        result = min(result, res)
    return result
        

archinp = open(sys.argv[1])
canttests = int(archinp.readline())

for numtest in xrange(1,canttests+1):
    cantints = int(archinp.readline())
    data1 = map(int, archinp.readline().split())
    data2 = map(int, archinp.readline().split())
    assert len(data1) == cantints
    assert len(data2) == cantints
    result = proc(data1, data2)
    print "Case #%d: %d" % (numtest, result)
