cycle = lambda x: x[-1] + x[:-1]

def getAll(n):
    res = []
    nS = str(n)
    for x in range(len(nS)):
        nS = cycle(nS)
        res.append(nS)
    res = map(int, list(set(res)))
    return filter(lambda x: x>n, res)


def isRecycled(n,m):
    n,m = str(n), str(m)
    if len(m)==1 or n==m:
        return False
    
    for x in range(len(m)):
        m = cycle(m)
        if m==n:
            return True
    return False

result = []
for x in range(int(raw_input(''))):
    total = 0
    [low, high] = map(int, raw_input('').split(' '))
    for n in range(low,high+1):
        total += len(filter(lambda x: n<x<=high, getAll(n)))
    print "Case #%d:"%(x+1), total
