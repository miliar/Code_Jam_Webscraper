import itertools
import sys

f = open(sys.argv[1],"r")
cases = int(f.readline())
for case in range(cases):
    a,b,k = map(int,f.readline().split())
    count = 0
    iters = itertools.product(range(a),range(b))
    for x,y in iters:
        if x & y < k:
            count += 1
    print "Case #"+str(case+1)+": "+str(count)
