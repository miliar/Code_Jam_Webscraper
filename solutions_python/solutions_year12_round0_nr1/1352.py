import sys
src = 'y qee ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jvz'
tgt = 'a zoo our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give upq'

d = dict()
for i in range(len(src)):
    d[src[i]] = tgt[i] 

n = int(sys.stdin.readline().strip())

for i in range(n):
    l = sys.stdin.readline()
    sys.stdout.write("Case #%d: " % (i+1))
    for c in l:
	if d.has_key(c):
	    sys.stdout.write(d[c])
	else:
	    sys.stdout.write(c)

