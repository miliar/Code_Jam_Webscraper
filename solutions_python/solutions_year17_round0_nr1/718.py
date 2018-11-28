rnd="p17Q"
pb="A"
size="Large"
fin=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.in"%(rnd,pb,size),'r')
fout=open("C:\F\workspace\Euler\EulerProject\GCJam\%s\%s-%s.out"%(rnd,pb,size),'w')

T=int(fin.readline())
print T
for i in range(1,T+1):
    S,sK=fin.readline().strip().split()
    K=int(sK)
    ix=0
    n=0
    while ix<=len(S)-K:
        if S[ix]=='-':
            n+=1
            for a in range(K):
                S=S[:ix+a] + ("-" if S[ix+a]=="+" else "+") + S[ix+a+1:]
        ix+=1
    res=str(n) if S.find("-")==-1 else "IMPOSSIBLE" 
            
    x=0
    line="Case #%d: %s" % (i, res)#
    print line
    fout.write(line+"\n")
fout.close()