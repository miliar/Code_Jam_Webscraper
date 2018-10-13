T = int(input())
res = []
for i in range(T):
    dn =str(input()).split()
    d = int(dn[0])
    n = int(dn[1])
    ksa = []
    time = 0
    for j in range(n):
        ks = input().split()
        k = int(ks[0])
        s = int(ks[1])
        ksa.append([k,s])
    for line in range(n):
        cind = n-1-line
        intsx = [[(ksa[lin][0]-ksa[cind][0])/(ksa[cind][1]-ksa[lin][1]),min(ksa[lin][1],ksa[cind][1])]for lin in range(n) if lin != cind and (ksa[cind][1]-ksa[lin][1]) != 0]
        ints = [c[0] for c in intsx if c[0] >= 0]
        dint = (d - ksa[cind][0])/ksa[cind][1]
        if len(ints) == 0:
            if dint > time:
                time = dint
        else:
            t = min(ints)
            if t < d:
                for aj in intsx:
                    if aj[0] == t:
                        mingrad = aj[1]
                        if ksa[cind][1] == mingrad:
                            if dint > time:
                                time = dint
            if ksa[cind][1]*t + ksa[cind][0] >= d:
                if dint > time:
                    time = dint
    res.append(d/time)
for r in range(T):
    print("Case #"+str(r+1)+': '+str(res[r]))
input()
