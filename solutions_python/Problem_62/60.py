import sys

def dbg(obj):
    print>>sys.stderr,obj

f = open('A-large.in')
cases_num = int(f.readline().strip())
for case in range(cases_num):
    print 'Case #%d:'%(case+1),
    #N,M=[int(s) for s in f.readline().split()]
    pts = int(f.readline().strip())
    pl = []
    for n in range(pts):
        pl.append([int(s) for s in f.readline().split()])
    pl.sort()
    #dbg(pl)
    rs=0
    for i in range(pts-1):
        for j in range(i+1,pts):
            if pl[i][1]>pl[j][1]:
                rs+=1
    print rs
f.close()    