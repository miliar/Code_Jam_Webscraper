#NK=0,0
#KN=1,1
#NNKK=0,0
#NKNK=0,1
#KKNN=2,2
#NNNKKK=0,0
#NNKNKK=0,1
#NNKKKN=1,1
#NKKNKN=1,2
#NKKKNN=2,2
#KNKKNN=2,3

S1=[]
S2=[]
W1=[]
W2=[]

def test1(N, K, cnt):
    global S1
    global W1
    if cnt==0:
        return 0
    s=""
    n=0
    k=0
    while n<cnt and k<cnt:
        if N[n]<K[k]:
            s+="N"
            n+=1
        else:
            s+="K"
            k+=1
    while n<cnt:
        s+="N"
        n+=1
    while k<cnt:
        s+="K"
        k+=1
    for i in range(0, len(S1)):
        if S1[i]==s:
            return W1[i]
#    print(N,K)
    best1=0
    k1=0
    for n in range(0,cnt):
        found=0
        win1=0
        for k in range(k1,cnt):
            if K[k]>N[n]:
                found=1
                break
        if found==0:
            win1=1
            k=0
        Nsave=N[:]
        Ksave=K[:]
        Ksave.remove(K[k])
        Nsave.remove(N[n])
        win1+=test1(Nsave, Ksave, cnt-1)
        if win1>best1:
            best1=win1
        if found==1:
            n+=1
            while n<cnt:
                if K[k]<N[n]:
                    break;
                n+=1
            n-=1
        else:
            n=cnt
            break
        k=k1
            
#    print(best1,n,k,N,K)
    S1.append(s)
    W1.append(best1)
    return best1

def test2(N, K, cnt):
    global S2
    global W2
    if cnt==0:
        return 0
#    print(N,K)
    s=""
    n=0
    k=0
    while n<cnt and k<cnt:
        if N[n]<K[k]:
            s+="N"
            n+=1
        else:
            s+="K"
            k+=1
    while n<cnt:
        s+="N"
        n+=1
    while k<cnt:
        s+="K"
        k+=1
    for i in range(0, len(S2)):
        if S2[i]==s:
            return W2[i]
    best2=0
    for k in range(0,cnt):
        for n in range(0,cnt):
            if N[n]>K[k]:
                Nsave=N[:]
                Ksave=K[:]
                Ksave.remove(K[k])
                Nsave.remove(N[n])
                best2=1+test2(Nsave, Ksave, cnt-1)
                S2.append(s)
                W2.append(best2)
                return best2
    k1=0    
    for n in range(0,cnt):
        for k in range(k1,cnt):
            if K[k]>N[n]:
                break
        Nsave=N[:]
        Ksave=K[:]
        Ksave.remove(K[k])
        Nsave.remove(N[n])
        win2=test2(Nsave, Ksave, cnt-1)
        if win2>best2:
            best2=win2
        n+=1
        while n<cnt:
            if K[k]<N[n]:
                break;
            n+=1
        n-=1
        k1=k
            
#    print(best2,n,k,N,K)
    S2.append(s)
    W2.append(best2)
    return best2
    
T=int(input())
for t in range(0,T):
    N=int(input())
    Naomi=sorted([float(x) for x in input().split()])
    Ken=sorted([float(x) for x in input().split()])
#    print("Naomi=",Naomi)
#    print("Ken=",Ken)
    best1=test1(Naomi,Ken,N)
    best2=test2(Naomi,Ken,N)
    print("Case #%d: %d %d"%(t+1,best2,best1))
