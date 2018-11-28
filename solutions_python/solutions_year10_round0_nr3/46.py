#from __future__ import division
import sys

def dbg(obj):
    print>>sys.stderr,obj

f=open('c:\\C-large.in')
case_num=int(f.readline().strip())
for cur_case in range(case_num):
    print 'Case #%d:'%(cur_case+1),
    R,k,N = [int(s) for s in f.readline().split()]
    dbg((R,k,N))
    pl = [int(s) for s in f.readline().split()]
    dbg(pl)
    cache=[[-1,-1] for _ in range(len(pl))]
    rk=0
    p=0
    r=0
    #dbg(cache)
    while cache[p][0]==-1:
    #while True:
        cache[p][0]=r
        cache[p][1]=rk
        #dbg(zip(pl,cache))
        k1=0
        c=0
        while k1+pl[p]<=k:
            k1+=pl[p]
            p+=1
            c+=1
            p%=N
            if c==N:break
        rk+=k1
        r+=1
        if r==R: break
        #dbg('begin at %d%s'%(p,cache[p]))
    if r==R:
        rs=rk
    else:
        #dbg('---------------')
        #dbg(cache[p])
        #dbg(r)
        #dbg(rk)
        #dbg(p)
        dR=r-cache[p][0]
        #dbg(dR)
        dRK=rk-cache[p][1]
        #dbg(dRK)
        #dbg('----------')
        #dbg((R-cache[p][0]))
        rs=(R-cache[p][0])/dR*dRK
        #dbg(rs)
        rest = (R-cache[p][0])%dR
        #dbg(rest)
        for pp in cache:
            if pp[0]==rest+cache[p][0]:
                rs+=pp[1]
                break
    print rs
f.close()