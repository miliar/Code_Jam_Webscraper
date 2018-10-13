import sys


d = dict((chr(i), 'X') for i in xrange(ord('a'), ord('z')+1))

data = [("ejp mysljylc kd kxveddknmc re jsicpdrysi","our language is impossible to understand"),
("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd","there are twenty six factorial possibilities"),
("de kr kd eoya kw aej tysr re ujdr lkgc jv","so it is okay if you want to just give up")]

for x in data:
  d.update(zip(*x))

d['z']='q'
d['q']='z'

lines = sys.stdin.readlines()
nr = 0
for line in lines[1:]:
  nr += 1
  print "Case #%d: %s" % (nr, ''.join(map(lambda x: d[x], line[:-1])))

