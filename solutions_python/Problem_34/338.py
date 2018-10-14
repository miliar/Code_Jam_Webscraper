
f = open('A-large.in', 'r').readlines()

l, d, n = f[0].strip().split(' ')
l, d, n = [int(x) for x in [l,d,n]]

# indexing
index = [{} for x in range(l)]
id = 0
for word in f[1:d+1]:
	id += 1
	for i in range(l):
		c = word[i]
		if not index[i].has_key(c):
			index[i][c] = set([id])
		else:
			index[i][c] = index[i][c].union(set([id]))

case = 1
for line in f[d+1:]:
	word = line.strip()
	k = 0
	ans = None
	for i in range(l):
		result = set()
		if word[k] == '(':
			k += 1
			while word[k] != ')':
				if index[i].has_key(word[k]):
					result = result.union(index[i][word[k]])
				k += 1
		else:
			result = result.union(index[i][word[k]])
		k += 1
		if ans == None:
			ans = result
		else:
			ans = ans.intersection(result)
			if len(ans) == 0:
				break
	print "Case #%d: %d" % (case, len(ans))
	case += 1

