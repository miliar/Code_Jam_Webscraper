import sys

bases = 'ejp mysljylc kd kxveddknmc re jsicpdrysi' + 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' + 'de kr kd eoya kw aej tysr re ujdr lkgc jv' + 'qz'
origs = 'our language is impossible to understand' + 'there are twenty six factorial possibilities' + 'so it is okay if you want to just give up' + 'zq'

T = int(sys.stdin.readline().strip())
for cs in xrange(1,T+1):
    line = list(sys.stdin.readline().strip())

    for i in xrange(len(line)):
        line[i] = origs[bases.find(line[i])]

    print 'Case #' + str(cs) + ':', ''.join(line)
