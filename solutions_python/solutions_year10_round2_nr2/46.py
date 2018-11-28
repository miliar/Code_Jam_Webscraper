import psyco
psyco.full()
def solve(endt):
    num_ur=0#number of unreach
    tot=0
    swap=0
    k=K
    for t in endt:
        if t>=B:
            swap+=num_ur
            k-=1
            if k==0:
                break;
        else:
            num_ur+=1
    return swap
            
fin = file( 'b.in' )
fout= file('b.out','w')
C=int(fin.readline().strip())
for c in range(C):
    N,K,B,T=[int(_) for _ in fin.readline().strip().split()]
    X=[int(_) for _ in fin.readline().strip().split()]
    V=[int(_) for _ in fin.readline().strip().split()]
    ENDT=[ x+v*T for x,v in zip(X,V)]
    #print ENDT
    #print map(lambda x:1 if x>=B else 0,ENDT )
    count=sum(map(lambda x:1 if x>=B else 0,ENDT ))
    if count<K:
        rst='Case #%d: IMPOSSIBLE\n'%(c+1)
    else:
        ENDT.reverse()
        out=solve(ENDT)
        rst='Case #%d: %d\n'%(c+1,out)
        
    print rst,
    fout.write(rst)
fout.close()
    
    