import sys

T = int(sys.stdin.readline())

def tester(x, r, c):
    if r > c:
        return tester(x, c, r)
    if x == 1:
        return 1
    if r * c % x != 0:
        return 0
    if c == 2:
        if x == 4:
            return 0
        return 1
    if c == 3:
        if r == 1 and (x == 1 or x == 3):
            return 0
        return 1
    if c == 4:
        if r == 4 :
            return 1
        if r == 1:
            if x == 2:
                return 1
            return 0
        if (r == 3 and (x == 3 or x == 2)) or (x == 2 and r == 2) or(x == 4 and r == 3):
            return 1
        return 0
    print("DAMN")


for j in range(T):
    X, R, C = map(int, sys.stdin.readline().strip().split())
    print("Case #" + str(j+1) + ": " + ("GABRIEL" if tester(X,R,C) else "RICHARD"))
