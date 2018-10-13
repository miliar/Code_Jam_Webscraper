import psyco
psyco.full()


def evalAnimal(name, tree, features, p, i):
	condition = tree[i]
	condition = condition.replace('(', '')
	condition = condition.replace(')', '')
	condition = condition.strip().split(' ')
	weight = float(condition[0])
	p = p * weight
	#print p

	if len(condition) == 1:
		print str(p)
	else:
		if condition[1] in features:
			#print name + ' is ' + condition[1]
			i = i + 1
		else:
			#print name + ' is not ' + condition[1]
			i = manySkip(tree, i)
			#print 'evaling ' + tree[i]
		evalAnimal(name, tree, features, p, i)

def manySkip(tree, i):
	parentes = 1
	while parentes != 0:
		i += 1
		parentes += tree[i].count('(')
		parentes -= tree[i].count(')')
		if parentes == 1:
			return i+1
		#print tree[i]

data = open('a.txt', 'r').read().split('\n')

(N,) = map(int, data.pop(0).split(' '))

for i in xrange(N):
	print 'Case #' + str(i+1) + ': '
	
	(L,) = map(int, data.pop(0).split(' '))
	
	tree = []
	for j in xrange(L):
		line = data.pop(0)
		if '))' in line:
			tree.append(line[:-1].strip())
			tree.append(')')
		else:
			tree.append(line.strip())
	(A,) = map(int, data.pop(0).split(' '))
	for j in xrange(A):
		info = data.pop(0).split(' ')
		name = info.pop(0)
		features = []
		for k in xrange(int(info.pop(0))):
			features.append(info.pop(0))
		evalAnimal(name, tree, features, 1, 0)
