fp=open("A-small.in.txt")
fw=open("A.small.out",'w')
T=int(fp.readline())
for i in range(1,T+1):
    n=fp.readline().split()
    m=fp.readline().split()
    A=int(n[0])
    B=int(n[1])
    p=[0]*A
    px=[0]*A
    pn=1
    for ii in range(A):
        p[ii]=float(m[ii])
        pn=pn*p[ii]
    for ii in range(A):
        px[ii]=1-p[ii]
    ret1=pn*(B-A+1)+(1-pn)*(B*2-A+2)
    ret2=B+2
    mini=ret1
    if ret2<mini:
        mini=ret2
    for ii in range(1,A+1):
        rpk=0
        for k in range(0,2**ii):
            rp=1
            s=str(bin(k))[2:]
            rs="0"*(A-len(str(s)))+s
            for iii in range(0,len(rs)):
                if rs[iii:iii+1]=="0":
                    rp=rp*p[iii]
                else:
                    rp=rp*px[iii]
            rpk=rpk+rp
        ret3=rpk*(B-A+2*ii+1)+(1-rpk)*(B-A+2*ii+1+B+1)
        if ret3<mini:
            mini=ret3
    print(mini)
    fw.write("Case #"+str(i)+": "+str(mini)+'\n')
fw.close()
fp.close()
    
    
