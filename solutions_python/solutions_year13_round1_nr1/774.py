import sys






def perfect(a):
    b = pow(a,0.5)
    if a == b*b:
        return True
    else:
        return False

def solve(r,t):
    D = pow(pow(2*r-1,2) + 8*t, 0.5)
    
    a = (-(2*r-1) + D)/4
    return int(a)

T = int(sys.stdin.readline())
k = 1
for casenum in xrange(T):
    a = sys.stdin.readline()
    #print a
    b = a.strip().split(' ')
    #print b
    r,t = int(b[0]), int(b[1])
    w = str(solve(r,t))
    s = "Case #%d: %s" % (k,w)
    print s
    k += 1

