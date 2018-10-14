def divide(n):
    res = (n-1)//2
    if n%2 == 1:
        return (res, res)
    return (res+1, res)

def lastseat(n, k):
    if k == 1:
        return divide(n)
    M, m = divide(n)
    occ = {M:0, m:0}
    occ[M]+= 1
    occ[m]+= 1
    k = k-1
    blocksize = 2
    #print(occ, k, blocksize)
    while blocksize < k:
        newocc = {}
        if len(occ) == 2:
            M, m = max(occ), min(occ)
            M1, m1 = divide(M)
            M2, m2 = divide(m)
            for q in M1, m1, M2, m2:
                newocc[q] = 0
            newocc[M1]+= occ[M]
            newocc[m1]+= occ[M]
            newocc[M2]+= occ[m]
            newocc[m2]+= occ[m]
        elif len(occ) == 1:
            M = max(occ)
            M1, m1 = divide(M)
            newocc[M1] = 0
            newocc[m1] = 0
            newocc[M1]+= occ[M]
            newocc[m1]+= occ[M]
        else:
            raise Exception
        occ = newocc
        k-= blocksize
        blocksize*= 2
        #print(occ, k, blocksize)
    #print(occ, k, blocksize)
    M, m = max(occ), min(occ)
    if k <= occ[M]:
        return divide(M)
    return divide(m)

for T in range(int(input())):
    n, k = map(int,input().split())
    M, m = lastseat(n, k)
    print("Case #%d: %d %d"%(T+1,M,m))