import sys
sys.setrecursionlimit(200000)
f = open(sys.argv[1])
N = int(f.readline())

def memo(f):
    d = {}
    def g(*args):
        if args not in d:
            d[args] = f(*args)
        return d[args]
    return g


@memo
def cd(n):
    #print n
    if(n < 10):
        return n
    elif(n % 10 == 0):
        return 1+cd(n-1)
    else:
        rev = int(str(n)[::-1])
        if rev < n:
            return min(1+cd(rev), 1+cd(n-1))
        else:
            return 1+cd(n-1)



for t in xrange(1,N+1):
    s = int(f.readline().strip("\n"))
    print "Case #%d: %d" % (t,cd(s))


        










