# Author: BAIZHIJIE (baizhj@gmail.com)

def solve_problem_c(r, k, q):
    run = 0
    sun = 0
    t = []
    lq = len(q)
    while True:
        i = 0
        s = 0
        while True:
            if s+q[i]<=k:
                s = s+q[i]
            else:
                break
            i = i+1
            if i>=lq:
                return r*s
        if q+[s] in t:
            pos = t.index(q+[s])
            va = sum([x[-1] for x in t[:pos]])
            vb = ((r-pos)/(run-pos))*sum([x[-1] for x in t[pos:]])
            vc = sum([x[-1] for x in t[pos:pos+((r-pos)%(run-pos))]])
            # print t, va, vb, vc, r-pos, run-pos, run, pos
            return (va+vb+vc)
        else:
            t.append(q+[s])
        run = run+1
        sun = sun+s
        q = q[i:]+q[:i]
        if run>=r:
            return sun

if __name__ == '__main__':
    n = int(raw_input())
    i = 0
    while i<n:
        rkn = raw_input()
        rkn = [int(x) for x in rkn.split()]

        gs = raw_input()
        gs = [int(x) for x in gs.split()]

        r = solve_problem_c(rkn[0], rkn[1], gs)

        print 'Case #%d: %d' % (i+1, r)
        i = i+1
