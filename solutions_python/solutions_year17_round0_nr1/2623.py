fin=open("A-large.in","r")
fout=open("A-large.out","w")
fread=fin.readline

for tcase in range(1,int(fread().strip())+1):
    inp=fread().strip().split()
    s=inp[0]
    k=int(inp[1])
    
    s=s.replace("+","1")
    s=s.replace("-","0")
    
    n=len(s)
    sn=int(s,2)
    
    xr=int("1"*k,2)
    x=1
    ans=0
    
    for i in range(n-k+1):
        if sn&x==0:
            ans+=1
            sn=sn^xr
        x*=2
        xr*=2
    
    #print(sn,file=fout)
    print("Case #%d: "%(tcase),end="",file=fout)
    if sn==2**n-1:
        print(ans,file=fout)
    else:
        print("IMPOSSIBLE",file=fout)

fin.close()
fout.close()