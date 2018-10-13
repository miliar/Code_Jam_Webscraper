from __future__ import print_function, division

title='d'

with open('%s.txt'%title) as fi, open('%s_o.txt'%title,'w') as fo:
    def readint():
        return int(fi.readline().strip())
    def readints():
        return list(map(int,fi.readline().split()))
    t=readint()
    for icase in range(1,t+1):
        def print_case(*args):
            print('Case #%d:'%icase,*args,file=fo)
        n=readint()
        mat=""
        for i in range(n):
            mat+=fi.readline().strip()
        ftable=open('table%d.txt'%n)
        ans=n**2
        for code in range(2**(n**2)):
            bins=bin(code)[2:]
            bins='0'*(n**2-len(bins))+bins
            ok=all(bins[j]>=mat[j] for j in range(n**2))
            diff=sum(bins[j]>mat[j] for j in range(n**2))
            res=ftable.readline().strip()
            if ok and res=='O':
                ans=min(diff,ans)
        print_case(ans)
