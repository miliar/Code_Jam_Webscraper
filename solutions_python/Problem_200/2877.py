def findFirstMisOrder(n, nLen):
    for i in xrange(nLen - 1):
        if int(n[i]) > int(n[i + 1]):
            return i + 1

    return nLen + 1

def change(n, misIdx, nLen):
    for i in xrange(misIdx, nLen):
        n[i] = "9"

    bIdx = misIdx - 1
    n[bIdx] = str(int(n[bIdx]) - 1)
    if bIdx != 0 and int(n[bIdx]) < int(n[bIdx - 1]):
        solve(n)
    return n

def findLeadNotZeroPos(n, nLen):
    for i in xrange(nLen):
        if int(n[i]) != 0:
            return i
    return i

def solve(n):
    nLen = len(n)
    misIdx = findFirstMisOrder(n, nLen)
    #print "misIdx:", misIdx, "nLen:", nLen

    if misIdx <= nLen:
        n = change(n, misIdx, nLen)

    notZeroIdx = findLeadNotZeroPos(n, nLen)
    return ''.join(map(str,n[notZeroIdx:]))


T=int(raw_input())
for cas in xrange(1,T+1):
    strN=str(raw_input())
    print "Case #{}: {}".format(cas,solve(map(int, strN)))

#("1{0:0>"+str(sub-2)+"b}1").format(i)
#("1{0:07b}1").format(10)

#print "Case #1:"
#for i in res:
#    print i," ".join(divs)





