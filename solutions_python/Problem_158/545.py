import sys

def input():
    T = int(sys.stdin.readline())
    for i in range(1,T+1,1):
        X,R,C = map(int, sys.stdin.readline().split())
        print "Case #{}: {}".format(i,omino(X,R,C))

def omino(X,R,C):
    if X == 1:
        return 'Gabriel'
    if X == 2:
        tot = R * C
        if tot % 2 == 0:
            return 'Gabriel'
        else:
            return 'Richard'
    if X == 3:
        if C == 1 or R == 1:
            return 'Richard'
        tot = R * C
        if tot % 3 == 0:
            return 'Gabriel'
        else:
            return 'Richard'
    if X == 4:
        if C == 1 or R == 1 or C == 2 or R == 2:
            return 'Richard'
        tot = R * C
        if tot % 4 == 0:
            return 'Gabriel'
        else:
            return 'Richard'
input()