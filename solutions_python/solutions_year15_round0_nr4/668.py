import sys
import math

if len(sys.argv) > 1:
    inf = open(sys.argv[1])
else:
    inf = open('d.in')

T = int(inf.readline())

for x in range(1,T+1):
    X, R, C = map(int, inf.readline().split(' '))

    if X >= 7: 
        can = True
    elif (R*C) % X != 0:
        can = True
    elif min(R, C) < math.ceil(X/2.):
        can = True
    elif X > max(R, C):
        can = True
    elif X > 3 and min(R, C) == 2:
        can = True
    else:
        can = False
    

    # print X,R,C,can

    print 'Case #%d: %s' % (x, 'RICHARD' if can else 'GABRIEL')