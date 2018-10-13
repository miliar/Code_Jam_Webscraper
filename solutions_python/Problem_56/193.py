import sys,re,math
from multiprocessing import Pool

MULTI_PROCESSES_ENABLED = False

def task(args):

    testid,tbl,N,K = args

    newtbl = {}
    for k,v in tbl.items():
        newtbl[k] = re.sub("\.","", v)[::-1]

    mr = re.compile("R"*K)
    mb = re.compile("B"*K)
    r = False
    b = False

    # left to right
    for k,v in newtbl.items():
        if not r:
            if mr.search(v):
                r = True
        if not b:
            if mb.search(v):
                b = True
        if r and b:
            return (testid,"Both")

        v += "-" * (N - len(v))
        tbl[k] = v

    # top down
    for i in range(N):
        v = "".join([tbl[j][i] for j in range(N)])
        if not r:
            if mr.search(v):
                r = True
        if not b:
            if mb.search(v):
                b = True
        if r and b:
            return (testid,"Both")

    # diag
    a = []
    for i in range(N):
        v = ""
        for j in range(0,N-i):
            v += tbl[j][j+i]
        a.append(v)
        v = ""
        for j in range(0,N-i):
            v += tbl[j+i][j]
        a.append(v)
        v = ""
        for j in range(0,N-i):
            v += tbl[N-(i+j+1)][j]
        a.append(v)
        v = ""
        for j in range(0,N-i):
            v += tbl[j][N-(i+j+1)]
        a.append(v)

    for v in a:
        if not r:
            if mr.search(v):
                r = True
        if not b:
            if mb.search(v):
                b = True
        if r and b:
            return (testid,"Both")


    if r and b:
        ans = "Both"
    elif r:
        ans = "Red"
    elif b:
        ans = "Blue"
    else:
        ans = "Neither"

    return (testid,ans)

def parse_test_cases(filename):
    f = open(filename, "r")
    N = int(f.readline())
    for case in range(N):
        N,K = map(int, f.readline().split(" "))
        tbl = {}
        for i in range(N):
            tbl[i] = f.readline().strip()
        yield [case+1,tbl,N,K]

def output_result(res):
    for i in res: print "Case #%d: %s" % (i[0],i[1])

if __name__ == '__main__':
    if MULTI_PROCESSES_ENABLED:
        result = Pool().map(task,parse_test_cases(sys.argv[1]))
        result = sorted(result, cmp=lambda x, y:cmp(x[0], y[0]))
    else:
        result = [task(i) for i in parse_test_cases(sys.argv[1])]
    output_result(result)
