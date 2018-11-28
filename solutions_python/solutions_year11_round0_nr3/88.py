from sys import stdin

def solve(l):
    l.sort(reverse = True)
    bal = 0
    ret = 0
    for e in l[:-1]:
        bal ^= e
        ret += e
    if bal == l[-1]:
        return str(ret)
    return 'NO'

buf = []
for line in stdin:
    buf.insert(0, line)
N = int(buf.pop())
for i in range(1, N+1):
    buf.pop()
    print 'Case #' + str(i) + ':',
    print solve([int(e) for e in buf.pop().strip().split()])
