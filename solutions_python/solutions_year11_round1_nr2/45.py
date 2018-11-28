from collections import defaultdict
def g(D,l,DD):
##    print(D,l,DD)
    re=(0,min(D))
    j=0
    S=set("".join(D))
##    print(S)
    for i,c in enumerate(l):
        DS=defaultdict(list)
        if c in S:
##            print(c)
            for d in D:
                if c not in d:
                    DD[d]+=1
                S=(len(d),)+tuple(i for i,ci in enumerate(d) if ci==c)
                DS[S].append(d)
        if len(DS)>0:
            for S in DS:
                for d in DS[S]:
                    D.remove(d)
                if len(DS[S])>1:
                    g(DS[S],l[i+1:],DD)
def f(D,L):
    Re=[]
    for l in L:
        DD={d:0 for d in D}
        g(D[:],l,DD)
        r=(D[0],DD[D[0]])
        for d in DD:
            if DD[d]>r[1]:
                r=(d,DD[d])
            elif DD[d]==r[1] and D.index(d)<D.index(r[0]):
                r=(d,DD[d])
        Re.append(r[0])
    return ' '.join(Re)
def main():
    fr=open('B-small-attempt5.in')
    fw=open('B-small-attempt5.out','w')
    s=next(fr)
    T=int(s)
    for i in range(T):
        s=next(fr)
        N,M=map(int,s.strip().split(' '))
        D=[]
        for j in range(N):
            s=next(fr)
            D.append(s.strip())
        L=[]
        for j in range(M):
            s=next(fr)
            L.append(s.strip())
        fw.write(str.format('Case #{0}: {1}\n',i+1,f(D,L)))
    fw.close()
main()
