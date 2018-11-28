import sys

input = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')

cases = input.readline()
cases = int(cases)

for x in range(cases):
	time = 0
	cur = input.readline()
	cur = cur.split()[1:]
	order = cur[::2]
	oranges = []
	blues = []
	for y in range(len(cur)):
		if cur[y] == 'O': oranges.append(cur[y+1])
		if cur[y] == 'B': blues.append(cur[y+1])
	
#	print order
#	print oranges
#	print blues
	
	bloc = 1
	oloc = 1
	
	while order:
		next = order[0]
		if blues: btar = int(blues[0])
		if oranges: otar = int(oranges[0])
		
		if next == 'B' and btar == bloc: 
			order = order[1:]
			blues = blues[1:]
		elif btar != bloc: bloc += (btar - bloc)/abs(btar - bloc)
		
		if next == 'O' and otar == oloc:
			order = order[1:]
			oranges = oranges[1:]
		elif otar != oloc: oloc += (otar - oloc)/abs(otar - oloc)
		time += 1
	
#	print time
		
	output.write("Case #%i: %i\n" % (x+1, time))

input.close()
output.close()


