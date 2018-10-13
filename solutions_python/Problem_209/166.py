import math
for t in range(int(input())):
    (N,K) = [int(i) for i in input().strip().split(' ')]
    P = [[int(i) for i in input().strip().split(' ')] for j in range(N)]
    for p in P: p.append(p[0]*p[1])
    H = sorted(P,key=lambda x:(x[2]),reverse=True)
    HB = sorted(H[0:K],key=lambda x:(x[0]),reverse=True)
    B = sorted(P,key=lambda x:x[0],reverse=True)
    #print(P,H,B)
    maxH = 0
    for i in range(K): maxH+=H[i][2]
    maxT = math.pi*(HB[0][0]**2)+2*math.pi*maxH
    if B[0] not in H[0:K]:
        maxNew = math.pi*(B[0][0]**2)+2*math.pi*(maxH-H[K-1][2]+B[0][2])
        if maxNew>maxT: maxT=maxNew
    print("Case #{0}: {1}".format(t+1,round(maxT,9)))
              
