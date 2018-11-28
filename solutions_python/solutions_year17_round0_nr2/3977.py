def isTidy(N):
    N = str(N)
    for i in xrange(len(N)-1):
        if N[i]>N[i+1]:
            return False
    return True

T = int(raw_input())
for t in xrange(T):
    S = int(raw_input())
    res = ''
    for i in xrange(S,0,-1):
        if isTidy(i):
            print "Case #{0}: {1}".format(t + 1, i)
            break
