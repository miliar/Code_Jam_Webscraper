import sys

fp = file(sys.argv[1])
tables = []
for i in xrange(int(fp.readline())):
	h, w = map(int, fp.readline().split(' '))
	tables.append([map(int, fp.readline().split(' ', w-1)) for i in xrange(h)])

def findDir(table):
	out = [[None]*len(table[0]) for i in xrange(len(table))]
	for y in xrange(len(table)):
		row = table[y]
		for x in xrange(len(row)):
			cell = row[x]
			neighbors = [
					table[y-1][x] if y > 0 else 1000, 
					table[y][x-1] if x > 0 else 1000, 
					table[y][x+1] if x < len(row)-1 else 1000, 
					table[y+1][x] if y < len(table)-1 else 1000, 
				]
			low = min(neighbors)
			if low < cell:
				for i in xrange(4):
					if neighbors[i] == low:
						out[y][x] = i
						break
	return out
tables = map(findDir, tables)

def propagate(table):
	out = [[None]*len(table[0]) for i in xrange(len(table))]
	def sub(y, x):
		if out[y][x] != None:
			return out[y][x]
		
		dir = table[y][x]
		if dir == None:
			out[y][x] = (y, x)
			return (y, x)
		else:
			next = ((y-1, x), (y, x-1), (y, x+1), (y+1, x))[dir]
			out[y][x] = next = sub(*next)
			return next
	
	for y in xrange(len(table)):
		row = table[y]
		for x in xrange(len(row)):
			if out[y][x] == None:
				sub(y, x)
	return out
tables = map(propagate, tables)

def assignLetters(table):
	out = [[None]*len(table[0]) for i in xrange(len(table))]
	cur = 0
	letters = {}
	for y in xrange(len(table)):
		row = table[y]
		for x in xrange(len(row)):
			dest = row[x]
			if dest not in letters:
				letters[dest] = chr(ord('a')+cur)
				cur += 1
			out[y][x] = letters[dest]
	return out
				
tables = map(assignLetters, tables)

for i in range(len(tables)):
	print 'Case #%i:' % (i+1)
	for row in tables[i]:
		print ' '.join(row)
