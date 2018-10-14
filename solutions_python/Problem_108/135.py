import sys
import cStringIO as StringIO

filename='A-small-attempt4'
#filename='A-large'
dir='/Users/larsr/Downloads/'
f = file(dir+filename+'.in')
#with sys.stdin as f:

stdout = sys.stdout
if 1:
    fileout = open(filename+'.out','w')
    sys.stdout = fileout

ff= StringIO.StringIO("""\
4
3
3 4
4 10
6 10
9
3
3 4
4 10
7 10
9
2
6 6
10 3
13
2
6 6
10 3
14
""")


memo={}

def swingit(holding_vine,reach):
    global D,d,l,memo
    if holding_vine in memo:
        r,val = memo[holding_vine]
        if r>reach and val==False:
            return val
        if r<reach and val==True:
            return val
        
    if reach>=D:
        memo[holding_vine]=True, reach
        return True

    reachable_vines = [i for i in range(N-1,-1,-1) if d[holding_vine]<d[i]<=reach]

    for v in reachable_vines:
        swing = min(d[v]-d[holding_vine], l[v])
        reach = swing + d[v]
        if swingit(v,reach):
            memo[holding_vine]=True, reach
            return True
    memo[holding_vine]=False, reach
    return False


T = int(f.readline())
for case in range(1,T+1):
    print 'Case #%d:' % case,
    N = int(f.readline().strip())
    d,l=[],[]
    for i in range(N):
        D,L = [int(x) for x in f.readline().strip().split()]
        d.append(D)
        l.append(L)
    D = int(f.readline().strip())
    holding_vine = 0
    reach=d[holding_vine]*2
    if swingit(holding_vine,reach):
        print 'YES'
    else:
        print 'NO'
    sys.stdout.flush()
    stdout.write('%d\n'%case)
    stdout.flush()

sys.stdout.close()
sys.stdout=stdout
