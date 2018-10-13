def go():
    f=open('D-small-attempt1.in')
    for x in range(int(f.readline())):
        print 'Case #%d: '%(x+1),solve(f)
    f.close()

def solve(f):
    n=int(f.readline().split()[1])
    c=[]
    k0=[int(x) for x in f.readline().split()]
    k=[0]*201
    for x in k0:
        k[x]+=1
    unopened=set()
    for x in range(n):
        line=f.readline().split()
        i=[int(j) for j in line]
        c.append((i[0],i[2:],x+1))
        unopened.add(x+1)
    res=r(k,c,[],{},unopened)
    if res:
        return ' '.join([str(x) for x in res])
    else:
        return 'IMPOSSIBLE'

def r(k,c,o,mem,unopened):
    if len(c)==0:
        return o
    tu=tuple(unopened)
    if tu in mem:
        return mem[tu]
    for x in c:
        if k[x[0]]:
            k1=list(k)
            c1=list(c)
            o1=list(o)
            unopened1=set(unopened)
            k1[x[0]]-=1
            unopened1.remove(x[2])
            del c1[c1.index(x)]
            o1.append(x[2])
            for y in x[1]:
                k1[y]+=1
            res=r(k1,c1,o1,mem,unopened1)
            if res:
                return res
    mem[tuple(unopened)]=0
    return 0
            
            
    
        
            
        
