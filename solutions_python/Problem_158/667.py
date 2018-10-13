import sys


def solve(x, r, c):

    R = min(r, c)
    C = max(c, r)
    
    rest = r*c-x
    
    if rest % x:
        return False
     
    if R == 1 and x > 2:
        return False
    if (C < x):
        return False
    if (x, R, C) in  [(4,2,4)]:
        return False

    return True

'''
for x in range(1, 5):
    for r in range(1, 5):
        for c in range(r, 5):
            print x, r, c, solve(x,r, c)
'''
if __name__ == "__main__":

    T = int(sys.stdin.readline())

    for t in range(T):

        X, R, C = map(int, sys.stdin.readline().split())
        res = solve(X, R, C)

        
        if not res:
            print "Case #%d: RICHARD" % (t+1)
        else:
            print "Case #%d: GABRIEL" % (t+1)
