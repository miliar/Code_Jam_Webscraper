import sys

def cutcost(vals, c):
    cost = 0
    for v in vals:
        cost += max(0, (v-1) // c)
    return cost

def run(pq):
    vals = [int(x) for x in pq.split()]
    minn = 10001
    for c in range(1,1002):
        minn = min(cutcost(vals, c) + c, minn)
    return minn

fin = open(sys.argv[1])

T = int(fin.readline().strip())
for i in range(1,T+1):
    xxx = int(fin.readline().strip())
    pq = fin.readline().strip()
    ans = run(pq)
    print('Case #%d: %s' % (i, ans))
