#Joe Snider
#4/16
#
#code jam 2017, r2Bb

#OK for small
def doit(N,Ni):
    #check max greater than sum of others (not right for large?)
    nm = max(Ni)
    if 2*nm > sum(Ni):
        return "IMPOSSIBLE"
    #place max (slow imp, OK up to 1000?)
    ret = []
    nmi = Ni.index(nm)
    Ni[nmi] = 0
    for i in xrange(nm):
        ret.append(nmi)
    #others go in first available gap
    for j in xrange(len(Ni)):
        n = Ni[j]
        if n >0:
            cLength = len(ret)
            insertI = -1
            for k in xrange(cLength):
                #if ret[(k+cLength-1)%cLength] != j and ret[(k+1)%cLength] != j:
                if ret[k] == ret[(k+1)%cLength]:
                    insertI = k
                    break
            insertI += 1
            for i in xrange(n):
                ret.insert(insertI, j)
                insertI = (insertI + 2) % len(ret)
            #print "gh2",ret
    translate = "ROYGBV"
    return "".join([translate[x] for x in ret])

#raw_imput is one line    
t = int(raw_input())
for i in xrange(1, t + 1):
    line = raw_input().split(" ")
    N = int(line[0])
    Ni = [int(x) for x in line[1:7]] #ROYGBV, order
    #print "gh1",N,Ni
    print "Case #%d: %s"%(i, doit(N,Ni))
