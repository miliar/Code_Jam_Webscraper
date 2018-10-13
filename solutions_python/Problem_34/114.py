import sys, os, re

f = file('A-large.in', 'r')
R = re.compile(r'(\(\w+?\)|\w)')

def norm(t):
    return [x.strip('()') for x in R.findall(t)]

def test_case(ncase):
    reg = norm(f.readline().rstrip())
    cnt = 0
    for i in words:
        ok = True
        for j, c in enumerate(i):
            if not c in reg[j]:
                ok = False
                break
        if ok:
            cnt += 1
    print 'Case #%d: %d' % (ncase, cnt)
    print >>sys.stderr, 'Case %d done' % ncase

(L, D, N) = map(int, f.readline().split())
words = []
for i in range(D):
    words.append(f.readline().rstrip())
for i in range(1, N+1):
    test_case(i)
