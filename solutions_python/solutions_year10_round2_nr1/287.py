import sys

def dbg(obj):
    print>>sys.stderr,obj

f = open('A-large.in')
cases_num = int(f.readline().strip())
for case in range(cases_num):
    print 'Case #%d:'%(case+1),
    N,M=[int(s) for s in f.readline().split()]
    dbg((N,M))
    dirs={}
    for n in range(N):
        path=f.readline().strip().split('/')[1:]
        dbg(path)
        curr=dirs
        for p in path:
            if p in curr:
                curr=curr[p]
            else:
                curr[p]={}
                curr=curr[p]
    rs=0
    for m in range(M):
        path=f.readline().strip().split('/')[1:]
        dbg(path)
        curr=dirs
        for p in path:
            if p in curr:
                curr=curr[p]
            else:
                curr[p]={}
                curr=curr[p]
                dbg('mkdir %s'%p)
                rs+=1
    print rs
f.close()