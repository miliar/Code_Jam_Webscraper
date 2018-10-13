# google codejam 2011 problem B : Magicka

def combine(x, y, combinations):
	for c in combinations:
		if (x==c[0] and y==c[1]) or (x==c[1] and y==c[0]):
			return c[2]
	return None
	
def opposesP(x, y, oppositions):
	for o in oppositions:
		if (x==o[0] and y==o[1]) or (x==o[1] and y==o[0]):
			return True
	return False
	
#  modifies sofar in situ!	
def invoke(sofar, combinations, oppositions, element):
	if sofar == []: 
		sofar[:] = [element]
		return
	c = combine(sofar[-1],element,combinations)
	if c is None:
		if any(map(lambda x: opposesP(x,element,oppositions),sofar)):
			sofar[:] = []
		else:
			sofar.append(element)
	else:
		sofar[-1] = c
		
T = int(raw_input())

case = 1
while case <= T:
	line = raw_input()
	pieces = line.split()
	p = 0
	C = int(pieces[p]); p += 1
	# get C triples
	combinations = [pieces[p+i] for i in range(C)]; p += C
	D = int(pieces[p]); p += 1
	oppositions  = [pieces[p+i] for i in range(D)]; p += D
	N = int(pieces[p]); p += 1
	series = pieces[p]
	
	sofar = []
	for element in series:
		invoke(sofar, combinations, oppositions, element)
	
	print "Case #%d: %s" % (case, "["+ ", ".join(sofar) + "]")
	case += 1
