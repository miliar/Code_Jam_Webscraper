import sys
import collections
import math

def rl():
    return tuple(map(int, raw_input().strip().split()))

RI = 'RICHARD'
GA = 'GABRIEL'
def solve(X, R, C):
    #print '====== ' + str(locals())
    if R*C < X: return RI
    if X>2 and R*C==X: return RI
    if (R*C)%X != 0: return RI
    
    if X == 1: 
        return GA
    if X == 2:
        return GA
    if X == 3: 
        return GA
    if X == 4:
        if not ((R == 2 and C == 4) or (R == 4 and C == 2)):
            return GA
        else:
            return RI

if __name__ == '__main__':
    for case in range(int(raw_input())):
        print 'Case #%d: %s' % (case+1, solve(*rl()))