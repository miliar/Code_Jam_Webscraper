import sys, os, operator


def solve(ws,player):
    (k,n)=(player,(player+1)%2)
    ki=len(ws[k])-1
    ni=ki
    kcount=0;
    while (ki>=0 and ni>=0):
        if ws[k][ki]>ws[n][ni]:
            (ki,ni)=(ki-1, ni-1)
            kcount+=1
        else:
            ni=ni-1
    if player==1:
        kcount=len(ws[k])-kcount
    return kcount



#f = open("sample-in.txt")
f = sys.stdin

cases = f.readline()
for case in xrange(1,int(cases)+1):
    f.readline()
    ws=[]
    ws.append(sorted(map(float,f.readline().split())))
    ws.append(sorted(map(float,f.readline().split())))
    k = solve(ws,0)
    n = solve(ws,1)

    print 'Case #%d: %d %d'%(case,k,n)







