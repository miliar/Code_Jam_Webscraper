import sys

def run(pq):
    p,q = pq.split()
    ints = [int(x) for x in q]
    needed = 0
    sofar = 0
    for c,x in enumerate(ints):
        needed = max(needed, c-sofar)
        sofar += x
    return needed


fin = open(sys.argv[1])

T = int(fin.readline().strip())
for i in range(1,T+1):
    pq = fin.readline().strip()
    ans = run(pq)
    print('Case #%d: %s' % (i, ans))
