import sys

def invoke(elem, li, combine, oppose):
	if len(li) == 0:
		li.append(elem)
		return li
	else:
		pair = (li.pop(), elem)
		if pair in combine.keys():
			li.append(combine[pair])
			return li	

		for e in li + [pair[0]]:
			if (e,elem) in oppose:
				return []
		
		li.extend([pair[0], pair[1]])
		return li


f = open(sys.argv[1])

T = int(f.readline().strip())

for i in xrange(T):
	tokens = f.readline().strip().split(' ')

	C = int(tokens.pop(0))
	combine = {} 
	for j in xrange(C):
		s = tokens.pop(0)
		combine[(s[0],s[1])] = s[2]
		combine[(s[1],s[0])] = s[2]

	D = int(tokens.pop(0))
	oppose = set() 
	for j in xrange(D):
		s = tokens.pop(0)
		oppose.add((s[0],s[1]))
		oppose.add((s[1],s[0]))

	N = int(tokens.pop(0))
	li = []
	elements = list(tokens.pop(0))
	for j in xrange(N):
		li = invoke(elements.pop(0), li, combine, oppose)
	
	print 'Case #%d: %s' % ((i+1), '[' + ', '.join(li) + ']')
		



		
	



