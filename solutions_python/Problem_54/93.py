import psyco
psyco.full()
def gcd(a,b):
    if a<b:
        a,b=b,a
    while b!=0:
        a,b=b,a%b
    return a
def gcds(ns):
    return reduce(gcd, ns)
fin=file('b.in')
fout=file('b.out','w')
T=int(fin.readline().strip())
for t in range(T):
    indata=[int(x) for x in fin.readline().strip().split()]
    N=indata[1]
    data=indata[1:]
    data.sort()
    data.reverse()
    ns=[data[i-1]-data[i] for i in range(len(data))][1:]
    g=gcds(ns)
    m=data[-1]
    rst=(g-m%g)%g
    out='Case #%d: %d\n'%(t+1,rst)
    print out,
    fout.write(out)
fout.close();