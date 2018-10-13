import math

CurrentPathIn = "small.in"
CurrentPathOut = "output"

fr = open(CurrentPathIn,"r")
fw = open(CurrentPathOut,"w")  

        
T = int(fr.readline())
for t in range(T):
    n, K = list(map(int, fr.readline().split()))
    R = [0]*n
    H = [0]*n
    for i in range(n):
        R[i], H[i] = list(map(int, fr.readline().split()))

    res = 0;
    for i in range(n):
        rm = R[i]
        L = [j for j in range(n) if R[j]<=rm and i!=j]
        if (len(L) >= K - 1):
            s1 = 0
            if (len(L)>0):
                L.sort(key = lambda x: (R[x]*H[x]), reverse = True)
                s1 = sum([R[x]*H[x] for x in L[:(K-1)]])
            s2 = 2*s1 + rm*(rm+2*H[i])
            if s2 > res:
                res = s2

    res *= math.pi
    res = format(res, '.8f')
    res = str(res)

    print("Case #"+str(t+1)+": "+res+"\n")
    fw.write("Case #"+str(t+1)+": "+res+"\n")

fr.close()
fw.close()
