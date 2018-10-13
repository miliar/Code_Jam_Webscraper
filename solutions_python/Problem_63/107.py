from __future__ import division
import sys, math
f = open(sys.argv[1])
cases = int(f.readline())
def nums(f):
    return [int(x) for x in f.readline().split()] 

def compute(L, P, C):
    tests = 0
    # T(L) == True
    # T(P) == False
    # If P <= L*C then T(L) and not T(L*C), so no test necessary
    # Test points are at L * C**i or ceil(P / C**i)
    # Then do binary search over test points
    # 
    if P <= L*C:
        return 0
    left, right = L, P
    #print low, high
    ml, dl = [], []
    while left*C < right:
        oleft, oright = left, right
        left = left*C
        right = int(math.ceil(right/C))
        if right <= left:
            if len(ml) < len(dl):
                ml.append(left)
            else:
                dl.append(right)
        else:
            ml.append(left)
            dl.append(right)
    dl.reverse()
    S = ml + dl
    #print len(ml), len(dl), S
    tests = math.ceil(math.log(len(S)+1)/math.log(2))
    return tests

for case in range(1,cases+1):
    L, P, C = nums(f)
    tests = compute(L,P,C)
    print "Case #%d: %d" % (case, tests)

