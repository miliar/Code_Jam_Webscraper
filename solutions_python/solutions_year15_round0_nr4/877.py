
import sys

T = int(sys.stdin.readline())

def g(X, R, C):
    L = sorted([R, C])

    if X == 1:
        return True
    if X == 2:
        return True
    if X == 3:
        return L not in [[1, 3]]
    if X == 4:
        return L not in [[1, 4], [2, 2], [2, 4]]

for i in range(T):
    X, R, C = [int(x) for x in sys.stdin.readline()[:-1].split(" ")]

    print "Case #%s: %s" % (i+1, "GABRIEL" if R*C % X == 0 and g(X, R, C) else "RICHARD")
