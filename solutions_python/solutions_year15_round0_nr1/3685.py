f=open('A-small-attempt1.in')
no_cases=int(f.readline())
g=open('solution.txt','w')
for i in range(no_cases):
    s=f.readline()
    m=s.replace("\n","")
    n=s.replace(" ","")
    msl=int(n[0])
    print msl
    ss=list(n[1:msl+2])
    ssint=map(lambda x : int(x),ss)
    print ssint
    ans=0
    if ssint[0]==0:
        ssint[0]=1
        ans=ans+1
    for j in range(1,msl+1):
        if ssint[j]==0:
            pass
        else:
            ps=ssint[0:j]
            sumps=sum(ps)
            if j > sumps:
                ans=ans+(j-sumps)
                ssint[j-1]=ssint[j-1]+(j-sumps)        
    print ssint
        
    op='Case #{0}: {1}'.format(i+1,str(ans))
    g.write(op)
    g.write('\n')
    print op
g.close()
    
    
