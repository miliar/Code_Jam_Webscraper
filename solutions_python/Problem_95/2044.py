import sys

a = list(('our language is impossible to understand'
          'there are twenty six factorial possibilities'
          'so it is okay if you want to just give upz'))
b = list(('ejp mysljylc kd kxveddknmc re jsicpdrysi'
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
          'de kr kd eoya kw aej tysr re ujdr lkgc jvq'))
d = dict(zip(b,a))
d['z'] = 'q'

lines = sys.stdin.readlines()
n = int(lines[0]) + 1

for i in xrange(1, n):
    print 'Case #%d: %s' % (i, ''.join([d[x] for x in lines[i][:-1]]))
