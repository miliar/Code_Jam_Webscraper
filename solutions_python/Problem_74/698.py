

fp = open('A-large.in', 'r')
n = int(fp.next())

x = 1

for line in fp:
	pos = { 'O': 1, 'B': 1 }

	last = None
	moved = 0

	result = 0

	o = line.split()[1:]
	
	while len(o) > 0:
		rb = o.pop(0)
		bt = int(o.pop(0))
		
		have_to_move = abs(pos[rb] - bt) + 1
		
		if rb == last:
			moved += have_to_move
			result += have_to_move
		else:
			if have_to_move > moved:
				result += have_to_move - moved
				moved = have_to_move - moved
			else:
				moved = 1
				result += 1
		
		pos[rb] = bt
		last = rb
		
		#print rb, bt, 'result:', result

	print 'Case #' + str(x) + ':', result
	x += 1

