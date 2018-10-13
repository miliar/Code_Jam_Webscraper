import sys

# possible = gabriel
# impossible = richard
def run(pq):
    g = ['GABRIEL', 'RICHARD']
    x,r,c = [int(x) for x in pq.split()]
    if r*c % x != 0:
        return g[1]

    if x == 1:
        return g[0]
    if x == 2:
        return g[0]
    if x == 3:
        if r == 1 or c == 1:
            return g[1]
        return g[0]
    if x == 4:
        if r == 3 and c == 4:
            return g[0]
        if r == 4 and c == 4:
            return g[0]
        if r == 4 and c == 3:
            return g[0]
        return g[1]

fin = open(sys.argv[1])

T = int(fin.readline().strip())
for i in range(1,T+1):
    pq = fin.readline().strip()
    ans = run(pq)
    print('Case #%d: %s' % (i, ans))
