import string

s = open('in.in').read().split('\n')[1:-1]
ans = []
let = {}
for ss in s:
#	print ss
	for c in ss:
		if c != ' ':
			let[c] = let.get(c, 0) + 1

i = 0
for ss in s:                            #"abcdefghijklmnopqrstuvwxyz"
	news = ss.translate(string.maketrans("ynficwlbkuomxsevzpdrjgthaq", "abcdefghijklmnopqrstuvwxyz"))
	i += 1
	print 'Case #%d: %s' % (i, news)

#print sorted(let.items(), key = lambda x: (-x[1], x[0]))
