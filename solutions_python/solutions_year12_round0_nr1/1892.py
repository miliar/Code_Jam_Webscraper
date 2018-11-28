import string

start = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv'''

end = '''our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up'''

d = {}
d['a'] = 'e'
d['y'] = 'a'
d['q'] = 'z'
d['z'] = 'q'

for cs, ce in zip(start,end):
    if cs.isalpha():
        d[cs]=ce

t = string.maketrans(string.ascii_lowercase, "".join(map(d.__getitem__, string.ascii_lowercase)))

n = input()
for i in xrange(n):
    line = raw_input()
    print "Case #%d:" % (i+1), line.translate(t)