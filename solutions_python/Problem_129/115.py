MOD = 1000002013

def cost(o,e):
    m = -e-o
    return ((m*(2*N+1-m))//2)%MOD

T = int(input())

for case in range(1,T+1):
    print('Case #',case,': ',sep='',end='')
    N,M = [int(x) for x in input().split()]
    ts = []
    for i in range(M):
        o,e,p = [int(x) for x in input().split()]
        ts.append((o,-e,p))
    ts.sort()
    original = (sum([p*cost(o,e) for o,e,p in ts]))%MOD
    finalts = []
    while True:
        newts = ts[:]
#        print(ts,finalts)
        for i,(o1,e1,p1) in enumerate(ts):
            flag = True
            for j,(o2,e2,p2) in enumerate(ts):
                if j<=i:
                    continue
                if o1<o2<=-e1<-e2:
#                    print(ts,newts,i,j)
                    del newts[j]
                    del newts[i]
#                    print("deleted",i,j,"successfully, flag should now be true")
                    p = min(p1,p2)
                    newts.extend([(o1,e2,p),(o2,e1,p),(o1,e1,p1-p),(o2,e2,p2-p)])
                    flag = False
                    break
#            print(flag)
            if flag:
                finalts.append(ts[i])
#                print(i, newts)
                del newts[i]
            break
        ts = sorted([t for t in newts if t[2]>0])
        if not ts:
            break
    best = (sum([p*cost(o,e) for o,e,p in finalts]))%MOD
#    print(original,best)
    print((original-best)%MOD)
