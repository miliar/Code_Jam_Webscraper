fin = open('B-large.in','r')
fout = open('B.out','w')
t=int(fin.readline())
INF=20000000000000000000
for cas in xrange(1,t+1):
    d=int(fin.readline())
    p=map(int,fin.readline().split())
    best=INF
    for sz in xrange(1,1001):
        best=min(best,sz+sum((i+sz-1)/sz-1 for i in p))
    fout.write("Case #{}: {}\n".format(cas,best))
fin.close()
fout.close()
