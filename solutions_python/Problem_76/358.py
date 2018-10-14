
ifile = open('../input/C-large.in', 'r')
ofile = open('../output/C-large.out', 'w')

cases = int(ifile.readline())

for case in xrange(cases):
    
    n = int(ifile.readline())
    xsum = 0
    isum = 0
    minval = None
    for sval in ifile.readline().split():
        val = int(sval)
        xsum ^= val
        isum += val
        minval = val if minval is None else min(minval, val)
    if xsum:
        result = 'NO'
    else:
        result = str(isum-minval)
    ofile.write('Case #%d: %s' % (case+1, result))
    ofile.write('\n')
    
    