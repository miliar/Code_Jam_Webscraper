from sys import stdin as I

T = int(I.readline())
for C in xrange(T):
    a, b = [int(part) for part in I.readline().split()]
    p = [float(part) for part in I.readline().split()]
    
    #C: ENTER + retype + ENTER
    rv = 1 + b + 1

    #B/A:
    pr_all = 1
    for i in xrange(a+1):
        rv = min(rv, (a - i) + (b - i) + 1 + (1 - pr_all)*(b+1))
        if i < a:
            pr_all *= p[i]    

    print "Case #%d: %.8f" % (C+1, rv)