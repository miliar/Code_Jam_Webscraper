fr=open("C:\Users\lihua\Desktop\USACO_Camp\Google_Jam\Q17b\B-large.in","r")
wr=open("C:\Users\lihua\Desktop\USACO_Camp\Google_Jam\Q17b\B-large.out","w")

arraylines=fr.readlines()
case=int(arraylines[0])
for t in range(1,case+1):
    a=arraylines[t].split(' ')
    N=str(a[0])[:-1]
    #print N
    n=len(N)
    T=True
    tidy=int(N[0])*(10**(n-1))-1
    i=0
    while i+1<n:
        T=T and (N[i]<=N[i+1])

        if N[i]<N[i+1]:
            a=int(N[:i+2])*(10**(n-i-2))-1
            tidy=max(tidy,a)
            i+=1
        elif N[i]>N[i+1]:
            break
        else:
            i+=1
    if T:
        resultx="Case #"+str(t)+": "+N+"\n"
    else:
        resultx="Case #"+str(t)+": "+str(tidy)+"\n"
    #print T
    wr.write(resultx)
    #print resultx

fr.close()
wr.close()
