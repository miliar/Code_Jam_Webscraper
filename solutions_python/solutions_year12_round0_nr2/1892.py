fin=open("b_small.in","r")
fout=open("b.out","w")
cas=int(fin.readline())
for caseno in xrange(1,cas+1):
    rin=map(int,fin.readline().split())
    n,s,p=rin[:3]
    scores=rin[3:]
    done=0
    cand=0
    for i in scores:
        if(i>=3*p-2):
            done+=1
        elif(i>=p+2*max(p-2,0)):
            cand+=1
    fout.write("Case #"+str(caseno)+": "+str(done+min(cand,s))+"\n")
    
