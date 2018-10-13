
from string import maketrans
f = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upzq'
t = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvqz'
trans = maketrans(t, f)

T = int(raw_input())
for i in xrange(T):
	s = raw_input()
	print "Case #%i: %s"%(i+1, s.translate(trans))
