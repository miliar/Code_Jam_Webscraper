fin = open('B-large.in', 'r')
fout = open('final.out', 'w')
T = int(fin.readline())
lines = fin.readlines()
for i in range(T):
	comb = []
	opp = []
	final = []
	def combines(a,b):
		for j in range(len(comb)):
			if comb[j][0] == str(a)+str(b):
				return comb[j][1]
		return ''
	def opposed(a):
		for j in final:
			for k in range(len(opp)):
				if j == opp[k][0] and a == opp[k][1]:
					return True
		return False
	inst = lines[i].rstrip().split()
	C = int(inst[0])
	for j in range(C):
		ind = 1+j
		comb.append([inst[ind][:2],inst[ind][2]])
		comb.append([inst[ind][1::-1],inst[ind][2]])
	D = int(inst[1+C])
	for j in range(D):
		ind = 2+C+j
		opp.append([inst[ind][0],inst[ind][1]])
		opp.append([inst[ind][1],inst[ind][0]])
	N = int(inst[2+C+D])
	elem = inst[3+C+D]
	for j in range(len(elem)):
		if len(final) > 0:
			cb = combines(elem[j],final[-1])
			if cb != '':
				final.pop()
				final.append(cb)
			else:
				if opposed(elem[j]):
					final = []
				else:
					final.append(elem[j])
		else:
			final.append(elem[j])
	s = 'Case #' + str(i+1) + ': ['
	for j in range(len(final)):
		s += str(final[j])
		if j != len(final)-1:
			s += ', '
	s += ']\n'
	fout.write(s)
