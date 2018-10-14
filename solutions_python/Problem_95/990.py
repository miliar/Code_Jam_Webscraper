import re

def getht(googlerese, plaineng, dic):
	"get the mapping of Googlerese"
	g = list(googlerese)
	p = list(plaineng)

	for index in range(len(g)):
		if g[index] == ' ':
			continue
		else:
			dic[g[index]] = p[index]

	print dic

def translate(googlerese, dic):
	g = list(googlerese)
	p = []
	print g
	for index in range(len(g)):
		if g[index] == '\n':
			continue
		p.append(dic[g[index]])
	return ''.join(p)

dic = {' ': ' '}
getht("ejp mysljylc kd kxveddknmc re jsicpdrysi", "our language is impossible to understand", dic)
getht("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", "there are twenty six factorial possibilities", dic)
getht("de kr kd eoya kw aej tysr re ujdr lkgc jv", "so it is okay if you want to just give up", dic)
getht("yeq", "aoz", dic)
getht("z", "q", dic)

alphabet = "abcdefghijklmnopqrstuvwxyz"
print translate(alphabet, dic)

for index in range(26):
	if dic.has_key(alphabet[index]):
		print alphabet[index] + " -> " + dic[alphabet[index]]
	else:
		print alphabet[index] + " -> ?"

f = open("./A-small-attempt0.in", "r+")
o = open("./A-small.out", "w+")

t = int(f.readline())
index = 1
for g in f:
	print g
	result = "Case #" + str(index) + ": " + translate(g, dic)
	o.write(result + '\n')
	index = index + 1
	print result

f.close()
o.close()