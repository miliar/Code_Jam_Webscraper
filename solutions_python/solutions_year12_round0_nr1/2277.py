e = 'aoz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
g = 'yeq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

r = dict(zip(e, g))
rb = dict(zip(g, e))
t = 'abcdefghijklmnopqrstuvwxyz'

m1 = ''
m2 = ''
for c in t:
    if c not in r:
	m1 = c
    if c not in rb:
	m2 = c

r[m1] = m2

fin = open("a1.txt")
fout = open("a1-out.txt", "w")

c = fin.readline()

for i, l in enumerate(fin):
    fout.write("Case #{}: {}\n".format(i + 1, "".join(r[x] for x in l[:-1])))

