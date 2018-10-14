import sys
from math import sqrt

def is_pal(x):
    x = str(x)
    l_x = len(x)
    if l_x == 1: return True
    
    if l_x % 2:
        #odd length
        return x[:l_x/2] == x[l_x/2+1:][::-1]
    else:
        #even length
        return x[:l_x/2] == x[l_x/2:][::-1]

f = open(sys.argv[1])
cases  = int(f.readline().strip())

for i in xrange(1,cases+1):
    mn, mx = [ int(x) for x in f.readline().strip().split() ]
    answer = 0
    for j in xrange(mn, mx+1):
        s_j = sqrt(j)
        if int(s_j) != s_j: continue
        s_j = int(s_j)
        if is_pal(j) and is_pal(s_j): answer += 1
    print "Case #%d: %s"%(i, answer)
