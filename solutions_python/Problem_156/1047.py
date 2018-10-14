import sys

PIE = 9 + 1;


def calc(pies, max):
    nk = 0
    nj = 0
    pk = 0 # last
    pj = 0 #second last

    for i in reversed(range(max+1)):
        val = pies[i]
        if (val > 0 and pk == 0):
            pk = i # max pies
            nk = val
        elif (val > 0):
            pj = i
            nj = val
            break

    #print "calc", pies, max, pk,nk,pj,nj
    if pk == 1:
        return nk

    mid = (int)((pk + 1)/2)

    minv = pk
    for t in range(mid):
        mm = t+1
        pies2 = pies[:]
        pies2[pk] = 0
        pies2[mm] += nk
        pies2[pk - mm] += nk
        suc2 = mm if (mm > pj) else pj
        suc2 = suc2 if (suc2 > (pk-mm)) else (pk-mm)
        v = calc(pies2, suc2) + nk
        minv = v if (v < minv) else minv
        #print "minv", minv

    return minv


fi = sys.stdin
t = int(fi.readline())


for _t in range(t):
    
    pies = [ 0 for i in range(PIE) ]

    d = int(fi.readline())
    line = fi.readline().split()
    
    max = 0
    for p in line:
        _p = int(p)
        pies[_p] += 1
        if _p > max :
            max = _p
    
    #print "pies", pies

    ans = calc(pies,max)
    print "Case #%d: %d" % ((_t+1,ans))		

