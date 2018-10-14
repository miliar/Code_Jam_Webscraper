fin = open('A-large.in','r')
fout = open('A.out','w')
t=int(fin.readline())
INF=20000000000000000000
for cas in xrange(1,t+1):
    rawsmax,raws=fin.readline().split()
    n=int(rawsmax)
    s=map(int,raws)
    tot=0
    ans=0
    for i in xrange(len(s)):
        if tot<i:
            ans+=i-tot
            tot=i
        tot+=s[i]
    fout.write("Case #{}: {}\n".format(cas,ans))

fin.close()
fout.close()
