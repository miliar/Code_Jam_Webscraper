from sys import stdin

lines = stdin.readlines()
for i in xrange(0, int(lines[0])):
    s = 1 + i*10
    r1, r2 = int(lines[s]), int(lines[s+5])
    res = set(lines[s+r1].split()) & set(lines[s+5+r2].split())
    l = len(res)
    if l == 0:
        print 'Case #{}: Volunteer cheated!'.format(i+1)
    elif l == 1:
        print 'Case #{}: {}'.format(i+1, res.pop())
    else:
        print 'Case #{}: Bad magician!'.format(i+1)
