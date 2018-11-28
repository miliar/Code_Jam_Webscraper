from collections import deque
import sys

filename = sys.argv[1]

f = open('%s.in' % filename)
g = open('%s.out' % filename, 'w')

DEBUG = sys.argv[2] if len(sys.argv) >= 3 else False
def dlog(s, *n):
    if DEBUG:
        if n:
            print(s % tuple(n))
        else:
            print(s)

T = int(f.readline())
for t in range(T):
    dlog("Case %d", t)
    line = f.readline().strip().split()
    cakes = line[0]
    k = int(line[1])

    window = deque()
    total = 0 
    flips = 0

    for i in range(len(cakes)):
        dlog(i)
        if cakes[i] == '-' and total % 2 == 0 or cakes[i] == '+' and total % 2 == 1:
            window.append(True)
            dlog("flip")
            total += 1
            flips += 1
            if i > len(cakes) - k:
                flips = "IMPOSSIBLE"
                dlog("impossible")
                break
        else:
            window.append(False)

        if i > k - 2:
            if window.popleft():
                total -= 1

    g.write('Case #%d: ' % (t + 1))
    g.write(str(flips))
    g.write('\n')


