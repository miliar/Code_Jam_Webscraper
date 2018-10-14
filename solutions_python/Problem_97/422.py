def getRotations(w):
    l=list()
    nrot=len(str(w))
    for i in range(nrot):
        l.append(w[i:]+w[:i])
    return l

def solve(a,b):
    count=0
    d=dict()
    for n in range(a,b+1):
        add=True
        w=str(n)
        rl=getRotations(w)
        for r in rl:
            if r in d:
                d[r]=d[r]+1
                add=False
                break
        if add:
            d[w]=0

    for k in d:
        v=d[k]
        if(v>1):
            count+=v*(v+1)//2
        else:
            count+=v
    return count

finput='recyclednumbers.in'
foutput='recyclednumbers.out'

ifile=open(finput,"r")
ofile=open(foutput,"w")

T=int(ifile.readline().strip('\n'))
for i in range(T):
    a,b=[int(x) for x in ifile.readline().strip('\n').split()]
    r=solve(a,b)
    
    print('Case #'+str(i+1)+':',r,file=ofile)
    print('Case #'+str(i+1)+':',r)

ifile.close()
ofile.close()
