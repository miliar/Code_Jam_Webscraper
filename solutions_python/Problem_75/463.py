# -*- coding:utf-8 -*-
import sys

def solve(c,cl,d,dl,n,ns):
    res = []
    for i in ns:
        res.append(i)
        for cll, clf in cl:
            if len(res) >= 2:
                if cll == ''.join(res[-2:]) or cll == ''.join([res[-1],res[-2]]):
                    res = res[0:-2]
                    res.append(clf)
        for dl1, dl2 in dl:
            if len(res) >= 2:
                if (dl1 in res) and (dl2 in res):
                    res = []

    ret = "[" + ', '.join(res) + "]"
    return ret


if __name__=='__main__':
    fname = sys.argv[1]
    f = open(fname)

    t = int(f.readline().strip())
    for i in range(1,t+1):
        l = f.readline().strip().split(' ')
        c = int(l[0])
        ct = l[1:c+1]
        cl = [(ct[n][0:2], ct[n][2]) for n in range(c)]  if c > 0 else []
        l = l[c+1:]
        d = int(l[0])
        dt = l[1:d+1]
        dl = [(dt[n][0], dt[n][1]) for n in range(d)] if d > 0 else []
        l = l[d+1:]
        n = int(l[0])
        ns = [l[1][x] for x in range(n)]
        
        res = solve(c,cl,d,dl,n,ns)

        print "Case #%d: %s" % (i, res)
