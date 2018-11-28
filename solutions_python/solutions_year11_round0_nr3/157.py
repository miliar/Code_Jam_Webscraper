import sys
lines = sys.stdin.readlines()
for nt in xrange(1, int(lines[0])+1):
    values = [int(tok) for tok in lines[2*nt].split()]
    if reduce(lambda x, y: x^y, values) == 0:
        output = sum(values) - min(values)
    else:
        output = 'NO'
    print 'Case #%d: %s' % (nt, output)
