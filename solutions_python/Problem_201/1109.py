# -*- coding: utf-8 -*-

def solve(s):
    nk = s.split(' ')
    N = int(nk[0])
    K = int(nk[1])
    d = {N:1}
    while K > 0:
        maxd = max(d)
        kin = min(K, d[maxd])
        #print(kin)
        d[maxd] -= kin
        if d[maxd] == 0:
            d.pop(maxd, None)
        K -= kin
        newdlarge = int(maxd / 2)
        newdsmall = maxd - 1 - newdlarge
        for m in [newdlarge, newdsmall]:
            if m in d:            
                d[m] += kin
            else:
                d[m] = kin
    return str(newdlarge) + ' ' + str(newdsmall)


f = open('C-small-2-attempt0.in','r')
fo = open('result.txt','w')
t = int(f.readline())
for ti in range(t):
    s = f.readline()
    r = solve(s)
    rs = "Case #%d: %s\n" % (ti+1, r)
    print(rs)
    fo.write( rs )
fo.close()
f.close()