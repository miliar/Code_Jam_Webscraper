
filename = 'C-small-attempt1'

def solve(a, b):
    if a == b: return False
    if b / a > 1: return True
    return not solve(b % a, a)

fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
cases = int(fin.readline().strip())
for case in xrange(1, cases + 1):
    A1, A2, B1, B2 = [int(x) for x in fin.readline().strip().split()]
    s = 0
    for a in xrange(A1, A2 + 1):
        for b in xrange(B1, B2 + 1):
            if solve(min(a, b), max(a, b)): s += 1
    print s
    fout.write('Case #%d: %d\n' % (case, s))
fin.close()
fout.close()
