import math

t = int(raw_input())

def ispalin(s):
    for i in xrange(len(s) / 2):
        if s[i] != s[-1 - i]:
            return False
    return True

for i in xrange(t):
    a, b = map(int, raw_input().split())
    c = 0
    A = int(math.sqrt(a))
    B = int(math.sqrt(b)) + 1
    for n in xrange(A, B + 1):
        if n ** 2 < a: continue
        elif n ** 2 > b: break
        if ispalin(str(n)) and ispalin(str(n ** 2)):
            c += 1
    print 'Case #%d: %d' % (i + 1, c)
