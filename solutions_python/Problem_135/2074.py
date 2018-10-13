import sys, os, math, re

ioname = sys.argv[1]
f = open('%s.in' % ioname, 'r')
f2 = open('%s.out' % ioname, 'w')

t = int(f.readline().strip())

for k in range(0, t):
    cc = {}
    for i in range(1, 17):
        cc[str(i)] = 0
    print('Case #%d: ' % (k + 1), end='', file=f2)
    n = int(f.readline().strip())
    for i in range(0, 4):
        s = f.readline().strip().split(' ')
        if i == n - 1:
            for j in s:
                cc[j] += 1
    n = int(f.readline().strip())
    for i in range(0, 4):
        s = f.readline().strip().split(' ')
        if i == n - 1:
            for j in s:
                cc[j] += 1
    
    ans = []
    for i in range(1, 17):
        if cc[str(i)] >= 2:
            ans.append(i)
    if len(ans) == 0:
        print('Volunteer cheated!', file=f2)
    elif len(ans) > 1:
        print('Bad magician!', file=f2)
    else:
        print('%d' % ans[0], file=f2)
f.close()
f2.close()