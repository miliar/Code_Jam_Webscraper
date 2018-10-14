v = [line.strip().split() for line in open('a-large.in','r').readlines()]
l, d, n = [int(num) for num in v[0]]

v = [l[0] for l in v]

di = v[1:d+1]

te = v[d+1:d+n+1]

#print(l,d,n,di,te)

out = open('a-large.out', 'w')

case = 0
for t in te:
	case += 1
#	print(t)
	letters = [[] for i in range(l)]
	c = 0
	for i in range(l):
		if t[c] == '(':
			c += 1
			while t[c] != ')':
				letters[i].append(t[c])
				c += 1
		else:
			letters[i].append(t[c])
		c += 1

	lens = [len(v) for v in letters]
#	print(letters, lens)
	cnt = 0
	for word in di:
		i = 0
		while i < l and word[i] in letters[i]:
			i += 1
		if i == l:
			cnt += 1
#			print(word)
	print("Case #%d: %d" % (case, cnt), file = out)
#	print("Case #%d: %d" % (case, cnt))

