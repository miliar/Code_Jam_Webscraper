
import sys

def rot(n):
    if n%10000==0:
        sys.stderr.write(str(n)+'\n')
    res = []
    nn = str(n)
    for i in range(1,len(nn)):
        rt = nn[i:]+nn[0:i]
        rtt = int(rt)
        if rt[0]!='0' and n<rtt and not rtt in res:
            res.append(rtt)
    return res

tp = 2000001

rec = [(n,m) for n in range(1,tp) for m in rot(n)]

T = int(sys.stdin.readline())



for i in range(1,T+1):
    line = sys.stdin.readline().split()
    line = map(lambda x : int(x), line)
    A = line[0]
    B = line[1]

    print "Case #%d: %d" % (i, len(filter(lambda (n,m): A<=n<m<=B, rec)))






