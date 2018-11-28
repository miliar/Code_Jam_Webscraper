from sys import stdin

def transform(ret, trf):
    ch = False
    while True:
        for tr in trf:
            if tr[:2] == ret[-2:]:
                ret[-2:] = tr[2]
                ch = True
                break
        else:
            return ch

def oppose(ret, opp):
    last = ret[-1]
    for op in opp:
        if last in op:
            if op[1-op.index(last)] in ret:
                del ret[:]
                return

def solve(case):
    dat = case.strip().split()
    C = int(dat.pop(0))
    trf = [list(e) for e in dat[:C]]
    for i in range(C):
        trf.append([trf[i][1], trf[i][0], trf[i][2]])
    del dat[:C]
    D = int(dat.pop(0))
    opp = [list(e) for e in dat[:D]]
    del dat[:D]
    N = int(dat.pop(0))
    invoke = dat.pop(0)
    ret = []
    for e in invoke:
#        print ret
        ret.append(e)
        if not transform(ret, trf):
            oppose(ret, opp)
    return ret

buf = []
for line in stdin:
    buf.insert(0, line)
N = int(buf.pop())
for i in range(1, N+1):
    print 'Case #' + str(i) + ':',
    print ''.join(str(solve(buf.pop().strip())).split("'"))
