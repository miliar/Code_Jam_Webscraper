d = {}
offsets = {}

def numEuros(r,k,g,pos=0):
    if r==0: return 0
    if pos not in d:
        d[pos] = g[pos]
        curPos = (pos+1)%len(g)
        while g[curPos] <= k-d[pos] and pos != curPos:
            d[pos] += g[curPos]
            curPos = curPos+1
            if curPos == len(g): curPos = 0
        offsets[pos] = curPos
        if pos==curPos:
            return d[pos] * r
    return d[pos] + numEuros(r-1,k,g,offsets[pos])

for i in xrange(1,int(raw_input())+1):
    r,k,_ = (int(x) for x in raw_input().split())
    g = [int(x) for x in raw_input().split()]
    d.clear()
    offsets.clear()
    print "Case #%d: %d" % (i,numEuros(r,k,g))
