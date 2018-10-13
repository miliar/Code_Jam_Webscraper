noTests=int(input())
for i in range(1,noTests+1):
    r,c=map(int,input().strip().split())
    print("Case #{}:".format(i))
    last=False
    count=0
    for p in range(r):
        L=list(input().strip())
        flag=False
        for j in range(c):
            if L[j]=='?':
                if j==0 or L[j-1]=='?':
                    flag=True
                else:
                    L[j]=L[j-1]
            elif flag:
                char=L[j]
                flag=False
                for k in range(j):
                    L[k]=char
        if flag:
            if p==0:
                last=True
                count+=1
            elif not last:
                print(Lp)
            else:
                count+=1
            continue
        elif last:
            last=False
            Lp=''.join(L)
            for k in range(count+1):
                print(Lp)
            count=0
        else:
            Lp=''.join(L)
            print(Lp)
        
