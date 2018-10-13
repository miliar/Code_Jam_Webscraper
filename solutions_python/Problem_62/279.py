

infile = 'A-large.in'

fhi = open(infile, 'r')

fho = open('%s.out' % infile[:-3], 'w')

# 1st line is cases
cases = int(fhi.readline())

for case in range(cases):
	# one line for wire count
	wires = int(fhi.readline())
	
	intersections = 0
	
	wireList = [map(int, fhi.readline().split(' ')) for j in range(wires)]
	
	while wireList:
		wire = wireList.pop()
		
		for toCheck in wireList:
			if wire[0] < toCheck[0] and wire[1] > toCheck[1]:
				intersections += 1
				
			if wire[0] > toCheck[0] and wire[1] < toCheck[1]:
				intersections += 1
	
	print intersections
	
	fho.write('Case #%d: %d\n' % (case + 1, intersections))