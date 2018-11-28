import sys,re,math
from multiprocessing import Pool

MULTI_PROCESSES_ENABLED = False

def task(args):

    testid,exists,create = args
    
    exists.sort()
    create.sort()

    buf = ["",]
    for i in exists:
        a = i.split("/")
        for j in range(len(a)):
            path = "/".join(a[0:j+1])
            if path not in buf:
                buf.append(path)

    ans = 0
    for i in create:
        a = i.split("/")
        for j in range(len(a)):
            path = "/".join(a[0:j+1])
            if path not in buf:
                buf.append(path)
                ans += 1

    return (testid,"%d"%ans)

def parse_test_cases(filename):
    f = open(filename, "r")
    N = int(f.readline())
    for case in range(N):
        N,M = map(int, f.readline().split(" "))
        exists = []
        create = []
        for i in range(N):
            exists.append(f.readline().strip())
        for i in range(M):
            create.append(f.readline().strip())
        yield [case+1,exists,create]

def output_result(res):
    for i in res: print "Case #%d: %s" % i

if __name__ == '__main__':
    if MULTI_PROCESSES_ENABLED:
        result = Pool().map(task,parse_test_cases(sys.argv[1]))
        result = sorted(result, cmp=lambda x, y:cmp(x[0], y[0]))
    else:
        result = [task(i) for i in parse_test_cases(sys.argv[1])]
    output_result(result)
