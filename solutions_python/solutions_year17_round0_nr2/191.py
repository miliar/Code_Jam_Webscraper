def ls2int(l):
    ret=0
    for x in l:
        ret=ret*10+x
    return ret

with open('B-large.in','r') as f, open('out.txt','w') as fout:
    t=int(f.readline().strip())
    lines=[s.strip() for s in f.readlines()]
    for case,line in enumerate(lines):
        n=[int(c) for c in line]
        ok=False
        while not ok:
            ok=True
            for i in range(len(n)-1):
                if n[i+1]<n[i]:
                    for j in range(i+1,len(n)):
                        n[j]=9
                    for j in range(i,-1,-1):
                        if n[j]==0:
                            n[j]=9
                        else:
                            n[j]=n[j]-1
                            break
                    ok=False
                    break
        ans=0
        for digit in n:
            ans=ans*10+digit
        print('Case #%d:'%(case+1),ans,file=fout)
