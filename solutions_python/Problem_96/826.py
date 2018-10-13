import sys

def total(x, y, z):
	return x + y + z
	

def surprising(x, y, z):
	if abs(x - y) > 1:
		return True
	if abs(z - y) > 1:
		return True
	if abs(x - z) > 1:
		return True
	return False

def possible(total, p, s = False):
	if total >= max((p), (p * 3 - 2)):
		return True
	if s and total >= max((p), (p * 3 - 4)):
		return True
	return False
	
fil = open(sys.argv[1]).readlines()

fout = open('g.txt', 'w')

for i in range(1, len(fil)):
	spl = fil[i].split()
	spl = [int(x) for x in spl]
	numG = spl[0]
	numS = spl[1]
	ceiling = spl[2]
	totals = spl[3:]
	withs = 0
	without = 0
	for j in totals:
		#print i, ceiling, possible(i, ceiling), possible(i, ceiling, True)
		without += possible(j, ceiling)
		withs += possible(j, ceiling, True)
	fout.write("Case #" + str(i) + ": " + str(without + min(withs - without, numS)) + '\n') 