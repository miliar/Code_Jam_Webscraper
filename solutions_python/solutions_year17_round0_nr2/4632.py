def isTidy(n):
    def rec(ns):
        return len(ns) < 2 or (ns[0] <= ns[1] and rec(ns[1:]))
    return rec(list(str(n)))

def solv(n):
    return max(i for i in xrange(0, n + 1) if isTidy(i))

def printRes(case, result):
    print "Case #%d: %s"%(case, result)

t = int(raw_input())
for i in xrange(1, t + 1):
    n = int(raw_input())
    res = solv(n)
    printRes(i, res)
