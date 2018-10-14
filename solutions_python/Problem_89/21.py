def primes(n):
    if n<2:
        raise StopIteration
    else:
        yield 2
        l=[True for i in range((n-1)//2)]
        for i in range(len(l)):
            if l[i]:
                yield 2*i+3
                for j in range(3*i+3,len(l),2*i+3):
                    l[j]=False
ps=list(primes(40))
from math import log
def f(n):
    if n==1:
        return 0
    if n<4:
        return 1
    re=1
##    print(n)
    for p in ps:
##        print(p)
        if p*p>n:
            return re
        else:
            re+=int(log(n,p))-1
def main():
    with open('C-small-attempt0.in') as fin,\
         open('C-small-attempt0.out','w') as fout:
        rstr=lambda f:next(f).rstrip()
        rstrs=lambda f:rstr(f).split()
        rint=lambda f:int(next(f).rstrip())
        rints=lambda f:list(map(int,next(f).strip()))
        for i in range(rint(fin)):
            n=rint(fin)
            re=f(n)
            print(str.format("Case #{0}: {1}",i+1,re))
            print(str.format("Case #{0}: {1}",i+1,re),file=fout)
main()
