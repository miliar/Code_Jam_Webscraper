import re, sys

l, d, n = [int(i) for i in sys.stdin.readline().split()]

alp = [sys.stdin.readline() for _ in range(d)]

i = 1
for line in sys.stdin.xreadlines():
    line = line.replace('(', '[')
    line = line.replace(')', ']')
    #print line

    n = 0
    for a in alp:
        #print '"%s" "%s"'%(line, a)
        if re.match(line, a):
            n += 1
    print 'Case #%d: %d'%(i, n)
    i += 1
