import string

ifn = 'C-small-attempt0.in'
ofn = 'C-small-attempt0.out'

out_f = open(ofn, 'w')

with open(ifn, 'r') as in_f:
    tmax = int(in_f.readline())
    for t in range(0, tmax):
        c = string.split(string.rstrip(in_f.readline(), string.whitespace), ' ')
        a, b = int(c[0]), int(c[1])
        len_a, len_b = len(str(a)), len(str(b))
        nl, nld = [], []
        count = 0
        if (len_a == 1 or len_b == 1) or len_a != len_b:
            print 'Skip: %d %d' % (a, b)
            print 'Case #%d: 0' % (t+1)
            out_f.write('Case #%d: 0 \r' % (t+1))
            continue
        else:
            nl = [str(x) for x in xrange(a, b+1)]
            nld = [x+x for x in nl]
        for j in nld: # n
            for i in nl: # m
                if str(j).find(str(i)) != -1:
                    if str(j)[:len(str(i))] < i:
                        count += 1
        print 'Done: %d %d' % (a, b)
        print 'Case #%d: %d' % (t+1, count)
        out_f.write('Case #%d: %d\r' % (t+1, count))
        
    out_f.close()

