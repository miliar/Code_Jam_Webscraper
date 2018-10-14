f = open('C-small-1-attempt0.in', 'r')
f2 = open('C-small-output.out', 'w')
k=0
nn=int(f.readline())
for line in f:
    k=k+1
    if k>nn:
        break
    n=int(line.split()[0])
    kk=int(line.split()[1])
    if kk==n:
        f2.write("Case #"+str(k)+": 0 0"+'\n')
        
    else:
        L=[n]
        Max,Min=n,n
        for i in range(0,kk):
            p=max(L)
            if p%2==1:
                Min,Max=(p-1)//2,(p-1)//2
            else:
                Max=(p)//2
                Min=Max-1
            a=L.index(p)
            del(L[a])
            L+=[Max,Min]
        f2.write("Case #"+str(k)+": "+str(Max)+" "+str(Min)+'\n')
f.close()
f2.close()
