import math
for T in range(input()):
    N,K=map(int,raw_input().split())
    RH=sorted([map(int,raw_input().split()) for n in range(N)])

    R2HR=[r*(2*h+r) for r,h in RH]
    #print RH
    # print R2HR
    S1=[0]*(N+1)
    for k in range(1,K):
        S2=S1[:]
        for n in range(N):
            S2[n+1]=max(S1[n]+2.0*RH[n][0]*RH[n][1], S2[n])
        # print S2
        S1=S2[:]
    s=max([S1[n]+max(R2HR[n:]) for n in range(N)])
    # print s
    s=s*math.pi
    print "Case #{}: {:.9f}".format(T+1,s)
