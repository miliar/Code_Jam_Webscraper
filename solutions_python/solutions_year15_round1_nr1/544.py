e=open('C:\Users\Hicham\Desktop\entrer12.txt','r')
s=open('C:\Users\Hicham\Desktop\sorter12.txt','w')
N=int(e.readline())
for i in xrange(1,N+1):
    t=int(e.readline())
    k=map(int,e.readline().split())

    tt=[]
    for h in xrange(0,t-1):
        tt.append(k[h]-k[h+1])
    b=max(tt)
    s1=0
    s2=0
    for ii,j in enumerate(k[:t-1]):
        if j>k[ii+1]:
            s1+=j-k[ii+1]
        if j>=b:
            s2+=b
        else:
            s2+=j
    print >> s , "Case #"+str(i)+": "+str(s1)+" "+str(s2)





e.close()
s.close()
