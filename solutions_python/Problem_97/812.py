import string, sys

def recycled(x, y):
	if x == y:
		return False
	if len(x) != len(y):
		return False
	else: 
		for i in range(len(x)):
			x = x[len(x) - 1] + x[:len(x) - 1]
			if x == y: return True
	return False
		
fil = open(sys.argv[1]).readlines()

fout = open('g.txt', 'w')

for i in range(1, len(fil)):
	spl = fil[i].split()
	a = int(spl[0])
	b = int(spl[1])
	#print a, b
	total = 0
	x = 1
	base = len(str(b)) - len(str(a))
	for e in range(base + 1):
		low = max(a, 10**e)
		high = 10**(e + 1) - 1
		if e == base:
			high = b
		#print low, high	
		for x in range(low, high + 1):
			for y in range(x, high + 1):
				#if recycled(str(x), str(y)):
					#print x, y, recycled(str(x), str(y))
				total += recycled(str(x), str(y))
	fout.write("Case #" + str(i) + ": " + str(total) + '\n')
	
print recycled('12345', '34512')