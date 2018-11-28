import sys

def universe(s, q):
    ret = 0
    used = set()
    while q:
        used.add(q[0])
        if len(used) == len(s):
            ret += 1
            used = set([q[0]])
        del q[0]
    return ret

n = input()

for i in range(n):
    s = input()
    s = [sys.stdin.readline().strip() for x in range(s)]
    q = input()
    q = [sys.stdin.readline().strip() for x in range(q)]

    print 'Case #%d: %d' % (i+1, universe(s, q))
