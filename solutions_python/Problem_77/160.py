import sys
lines = sys.stdin.readlines()
for nt in xrange(1, int(lines[0])+1):
    initial = [int(tok) for tok in lines[2*nt].split()]
    final = sorted(initial)
    result = sum(initial[i] != final[i] for i in xrange(len(initial)))
    print 'Case #%d: %.6f' % (nt, result)
