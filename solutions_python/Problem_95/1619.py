a = {}
alpha = [chr(i) for i in range(97, 97 + 26)]
c = [1] * 3
p = [1] * 3
c[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi"
p[0] = "our language is impossible to understand"
c[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd"
p[1] = "there are twenty six factorial possibilities"
c[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv"
p[2] = "so it is okay if you want to just give up"

for i in range(3):
	for j in range(len(c[i])):
		#print c[i],
		if c[i][j] not in a:
			a[c[i][j]] = p[i][j]
a['z'] = 'q'
a['q'] = 'z'

f = open('input.txt')
n = int(f.read(2))
for i in range(n + 1):
	x = f.readline()
	x = list(x)
	x.remove('\n')
	s = ""
	for j in x:
		s += a[j]
	print "Case #%d: %s" % (i, s)
	