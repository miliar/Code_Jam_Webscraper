import sys

lines = [x.strip() for x in file(sys.argv[1], 'r').readlines()]

def naive(r, k, g):
	queue = list(g)
	total = 0
	for i in range(r):
		people = 0
		left = k
		riding = []
		while people < k and len(queue):
			if queue[0] <= left:
				x = queue.pop(0)
				total += x
				left -= x
				people += x
				riding.append(x)
			else:
				break
		
		queue += riding
	return total

def smart(r, k, g):
	grouptotal = sum(g)
	if k > grouptotal:
		return grouptotal * r
	
	packed = []
	queue = list(g)
	for i in range(len(g)*2):
		people = 0
		left = k
		total = 0
		riding = []
		while people < k:
			if queue[0] <= left:
				x = queue.pop(0)
				total += x
				left -= x
				people += x
				riding.append(x)
			else:
				break
		packed.append(total)
		queue += riding
	
	total = r // len(packed) * sum(packed)
	total += sum(packed[:r % len(packed)])
	return total

for i in range(1, int(lines[0])*2+1, 2):
	r, k, n = map(int, lines[i].split(' '))
	groups = map(int, lines[i+1].split(' '))[:n]
	
	grouptotal = sum(groups)
	#smarttotal = smart(r, k, groups)
	naivetotal = naive(r, k, groups)
	#assert smarttotal == naivetotal
	print 'Case #%i: %i' % (i / 2 + 1, naivetotal)
