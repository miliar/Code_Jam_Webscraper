with open('A-large.in','r') as f, open('a_out.txt','w') as fout:
    t=int(f.readline().strip())
    lines=[s.strip() for s in f.readlines()]
    for case,line in enumerate(lines):
        ss,ks=line.split()
        s=list(ss)
        k=int(ks)
        ans=0
        for i in range(len(s)-k+1):
            if s[i]=='-':
                s[i:i+k]=['-' if c=='+' else '+' for c in s[i:i+k]]
                ans+=1
        ok=s[-(k-1):]==['+']*(k-1)
        print('Case #%d:'%(case+1),ans if ok else 'IMPOSSIBLE',file=fout)
