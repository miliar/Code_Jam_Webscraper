f=open("/Users/nischal/Desktop/A-large.in",'r')
g=open("/Users/nischal/Desktop/output",'w')
t=int(f.readline())
for i in range(t):
    m,s1=f.readline().split()
    m=int(m)
    ans=0
    s=int(s1[0])
    for j in range(1,m+1):
        if j>s:
            ans+=(j-s)
            s+=(j-s)
        s+=int(s1[j])
    g.write("Case #"+str(i+1)+": "+str(ans)+'\n')
