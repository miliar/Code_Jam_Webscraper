from string import maketrans
import sys

s1='ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz'
s2='our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq'

t=maketrans(s1,s2)

#print s1.translate(t)

nlines=int(sys.stdin.readline())
i=0
for line in sys.stdin:
    i=i+1
    line=line.rstrip('\n')
    print 'Case #%(i)d: %(line)s' % {'i':i, 'line':line.translate(t)}
