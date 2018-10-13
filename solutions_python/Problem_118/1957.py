import sys
import math

with open(sys.argv[1]) as fh:
    T = int(fh.readline())
    for i in range(T):
        A, B = map(int, fh.readline().split())
        r = [j**2 for j in range(int(math.ceil(math.sqrt(A))), int(math.floor(math.sqrt(B))+1)) \
             if str(j)[::-1]==str(j) and str(j**2)[::-1]==str(j**2) ]
        print "Case #{0}: {1}".format(i+1, len(r))
