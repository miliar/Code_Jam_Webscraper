import sys
import math
sys.setrecursionlimit(10000)

f  = open('/home/alex/workspace/gcj_qual/D-small-attempt3.in')
fo = open('/home/alex/workspace/gcj_qual/dout.txt', 'wb')
T = int(f.readline())
for t in range(T):
    X, R, C = [int(x) for x in f.readline().strip().split(' ')]
    res = 'RICHARD'
    if X == 1:
        res = 'GABRIEL'
    if X == 2 and R*C % 2 == 0:
        res = 'GABRIEL'
    if X == 3 and R*C % 3 == 0 and (R >= 3 or C >= 3) and not (R==1 or C==1):
        res = 'GABRIEL'
    if X == 4 and R*C % 4 == 0 and (R >= 3 or C >= 3) and (R > 2 and C > 2):
        res = 'GABRIEL' 
    print "Case #%d: X=%d R=%d C=%d %s" % (t+1, X, R, C, res)
    fo.write("Case #%d: %s\n" % (t+1, res))
fo.close()
f.close()
    