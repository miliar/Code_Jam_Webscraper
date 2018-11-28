import sys

t = input()
cases = sys.stdin.readlines()
c = 1

def numrevs(x, A, B):
    total = 0
    for i in xrange(len(str(x))):
        tmp1 = str(x)[:i+1]
        tmp2 = str(x)[i+1:]
        y = int(tmp2 + tmp1)
        if x < y and A <= y <= B:
            total += 1
    
    return total

for case in cases:
    case = case.strip()
    if case:
        A, B = map(lambda x: int(x), case.split())
        total = 0

        for i in xrange(A, B + 1):
            total += numrevs(i, A, B)
        
        print 'Case #%d: %d' % (c, total)
        c += 1

