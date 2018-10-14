def f(N,PD,PG):
    if PD<100 and PG==100:
        return "Broken"
    if PD>0 and PG==0:
        return "Broken"
    possible=False
    for i in range(1,N+1):
        if (i*PD)%100==0:
            return "Possible"
    return "Broken"
def main():
    fr=open('A-large.in')
    fw=open('A-large.out','w')
    s=next(fr)
    T=int(s)
    for i in range(T):
        s=next(fr)
        N,PD,PG=map(int,s.strip().split(' '))
        fw.write(str.format('Case #{0}: {1}\n',i+1,f(N,PD,PG)))
main()
