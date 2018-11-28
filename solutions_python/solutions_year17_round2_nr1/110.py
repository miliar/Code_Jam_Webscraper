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
    D = int(line[0])
    N = int(line[1])

    max_time = 0
    for n in range(N):
    	line = f.readline().strip().split()
    	pos = int(line[0])
    	vel = int(line[1])
    	time = 1.0 * (D - pos) / vel
    	max_time = max(time, max_time)

    ans = D / max_time

    g.write('Case #%d: %f' % (t + 1, ans))
    g.write('\n')


