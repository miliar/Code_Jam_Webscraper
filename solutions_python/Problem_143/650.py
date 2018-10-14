

def combos(a,b,k):
	s = set()
	for i in range(0,a):
		for j in range(0,b):
			if (i & j) < k:
				s.add((i,j))
			else:
				continue
	return len(s)

if __name__ == '__main__':
	cases = int(raw_input())
	output = []
	for i in range(0,cases):
		l  = raw_input()
		a = int(l.split()[0])
		b = int(l.split()[1])
		k = int(l.split()[2])
		output.append(combos(a,b,k))
	for i in range(0,cases):
		print "Case #%d: %d"%(i+1,output[i])

