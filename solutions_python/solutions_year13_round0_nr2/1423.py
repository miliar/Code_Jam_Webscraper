fp = open("B-large.in")
fx = open("out.txt",'w+')
t = int(fp.readline())

for case in range(t):
    h = fp.readline().strip()
    N=int(h.split(" ")[0])
    M=int(h.split(" ")[1])
    
    a=[]
    b=[]
    for i in range(N):
        L=fp.readline().split(" ")
        for i in range(len(L)):
            L[i]=int(L[i])
        a.append(L)
    """for i in range(N):
        for j in range(M):
            
            b.append()
        a.append(b)"""
    flag1,flag2=0,0
    for i in range(N):
        for j in range(M):
            flag1=0
            for k in range(N):
                if (a[k][j]>a[i][j]):
                    flag1=1
                    break
            if (flag1==1):
                flag2=0
                for k in range(M):
                    if (a[i][k]>a[i][j]):
                        flag2=1
                        break
            if (flag1==1 and flag2==1):
                break
        if (flag1==1 and flag2==1):
                break
    if (flag1==0 or flag2==0):
        print("Case #"+str(case+1)+": "+"YES",file=fx)
    if (flag1==1 and flag2==1):
        print("Case #"+str(case+1)+": "+"NO",file=fx)
    
        

fp.close()
fx.close()
