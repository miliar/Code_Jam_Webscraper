import os, sys

ioname = sys.argv[1]
f = open('%s.in' % ioname, 'r')
f2 = open('%s.out' % ioname, 'w')

t = int(f.readline().strip())

for k in range(0, t):
    print('Case #%d: ' % (k + 1), end='', file=f2)
    sm, hist = f.readline().strip().split(' ')
    sm = int(sm)
    count = 0
    ans = 0
    for i, c in enumerate(hist):
        s = int(c)
        if i > count:
            ans += i - count
            count = i
        count += s
    print(ans, file=f2)
f.close()
f2.close()