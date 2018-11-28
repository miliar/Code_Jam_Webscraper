import sys

f = open(sys.argv[1],'r')
T = int(f.readline())

o = open('out','w')
for t in range(T):
	tokens = f.readline().split()

	combine = {}
	C = int(tokens[0])
	for c in range(C):
		cb = tokens[1+c]
		combine[cb[0]+cb[1]] = cb[2]
		combine[cb[1]+cb[0]] = cb[2]

	enemy= {}
	D = int(tokens[1+C])
	for d in range(D):
		en = tokens[2+C+d]
		enemy.setdefault(en[0], []).append(en[1])
		enemy.setdefault(en[1], []).append(en[0])
	
	N = int(tokens[2+C+D])
	ser = tokens[3+C+D]

	out = []
	for x in ser:
		if len(out) >= 1:
			if out[-1]+x in combine:
				out[-1] = combine[out[-1]+ x]
			elif x in enemy:
				for y in enemy[x]:
					if y in out: 
						out = []
						break
				else: out.append(x)
			else: out.append(x)
		else: out.append(x)

	o.write('Case #%d: [' %(t+1))
	if len(out):
		o.write(out[0])
		for i in range(len(out)-1):
			o.write(', %c' %out[i+1])
	o.write(']\n')

		


