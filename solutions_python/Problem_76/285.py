f = open('C-large.in', 'r')
cases = int(f.readline())
for case in range(cases):
    nCases = f.readline()
    line = f.readline()
    l = [int(s) for s in line.split()]

    xsum = reduce(lambda x,y: x^y, l)
    if xsum == 0:
        l.sort()
        print "Case #%s: %s" % (case+1, sum(l[1:]))
    else:
        print "Case #%s: NO" % (case+1)


