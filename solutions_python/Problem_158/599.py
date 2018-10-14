import sys
inp = sys.stdin.readline

def solve(X,L,R):
    if X == 1:
        return True
    elif X == 2:
        if L*R % 2 == 0:
            return True
        else:
            return False
    elif X == 3:
        if L*R % 3 != 0:
            return False
        else:
            if min(L,R) == 1 and max(L,R) == 3:
                return False
            else:
                return True
    elif X == 4:
        if L*R % 4 != 0:
            return False
        else:
            if min(L,R) == 1 and max(L,R) == 4:
                return False
            elif min(L,R) == 2 and max(L,R) == 2:
                return False
            elif min(L,R) == 2 and max(L,R) == 4:
                return False
            else:
                return True

for i in xrange(1, int(inp().strip())+1):
    X,L,R = map(int, inp().strip().split())
    if solve(X,L,R):
        print "Case #%d: GABRIEL" % (i)
    else:
        print "Case #%d: RICHARD" % (i)