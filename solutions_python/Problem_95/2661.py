import sys
from string import maketrans

s1 = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jvyeqz'''
s2 = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give upaozq'''

trans = maketrans(s1, s2)

for i, line in enumerate(open(sys.argv[1]).read().splitlines()[1:], 1):
    print 'Case #%d: %s' % (i, line.translate(trans))
