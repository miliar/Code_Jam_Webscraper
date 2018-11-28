def init():
	aux = ["ejp mysljylc kd kxveddknmc re jsicpdrysi", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "de kr kd eoya kw aej tysr re ujdr lkgc jv"]
	res = ["our language is impossible to understand", "there are twenty six factorial possibilities", "so it is okay if you want to just give up"]
	translate = {}
	for i in range(len(aux)):
		for j in range(len(aux[i])):
			if aux[i][j] not in translate:
				translate[aux[i][j]] = res[i][j]
	return translate

translate = init()
translate['z'] = 'q'
translate['q'] = 'z'
f = open("A-small-attempt1.in")
g = open("resultado.txt", 'w')
f.readline()
i = 1
for line in f:
	line = line.strip()
	aux = ""
	for c in line:
		aux += translate[c]
	g.write("Case #%s: %s \n" % (i, aux))
	i += 1