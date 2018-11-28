import sys
from string import maketrans

inp = "q a zoo ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
out = "z y qee our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

trantab = maketrans(inp, out)

#str = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
#print str.translate(trantab)

f = open('A-small-attempt6.in', 'r')
o = open('a.out', 'w')

T = int(f.readline().strip())

for t in xrange(T):
    s = f.readline()
    o.write("Case #{0}: {1}".format(t+1, s.translate(trantab)))
    

f.close()
o.close()

