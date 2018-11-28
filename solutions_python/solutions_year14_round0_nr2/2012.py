import sys, os, math, re

ioname = sys.argv[1]
f1 = open('%s.in' % ioname, 'r')
f2 = open('%s.out' % ioname, 'w')

t = int(f1.readline().strip())

for k in range(0, t):
    print('Case #%d: ' % (k + 1), end='', file=f2)
    s = f1.readline().strip().split(' ')
    c = float(s[0])
    f = float(s[1])
    x = float(s[2])
    
    n = (f * x - 2 * c) / (f * c)
    if n < 0:
        n = 0
    n = math.floor(n)
    t = 0.0
    for i in range(0, n):
        t += c / (2 + i * f)
    t += x / (2 + n * f)
    
    print('%.7f' % t, file=f2)
f1.close()
f2.close()