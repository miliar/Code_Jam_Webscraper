src = "ejp mysljylc kd kxveddknmc re jsicpdrysi" + "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd" + "de kr kd eoya kw aej tysr re ujdr lkgc jv"
dst = "our language is impossible to understand" + "there are twenty six factorial possibilities" + "so it is okay if you want to just give up"
d = dict()
d['z'] = 'q'
d['q'] = 'z'
for i in range(len(src)):
	if src[i] >= 'a' and src[i] <= 'z':
		d[src[i]] = dst[i]
f = open('file.in', 'r')
data = f.readlines()
for i in range(1, len(data)):
	data[i] = data[i][:-1]
	line = [' '] * len(data[i])
	for j in range(len(data[i])):
		if data[i][j] in d:
			line[j] = d[data[i][j]]
		else:
			line[j] = data[i][j]
	res = ''
	for c in line:
		res += c
	print 'Case #' + str(i) + ': ' + res
