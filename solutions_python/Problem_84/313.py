import math

#f = file("A-test.in", "r")
#f = file("/Users/finn/Downloads/A-small-attempt0.in", "r")
f = file("/Users/finn/Downloads/A-large.in", "r")
#of = file("A-test.out", "w")
#of = file("A-small.out", "w")
of = file("A-large.out", "w")
lines = f.readlines()

def passover(m):
	for y in range(0, len(m) - 1):
		for x in range(0, len(m[y]) - 1):
			if m[y][x] == '#' and (x == 0 or m[y][x - 1] != '#') and (y == 0 or m[y - 1][x] != '#'):
				if m[y][x + 1] == '#' and m[y + 1][x] == '#' and m[y + 1][x + 1] == '#':
					m[y][x] = '/'
					m[y][x + 1] = '\\'
					m[y + 1][x] = '\\'
					m[y + 1][x + 1] = '/'
					
	left = 0
	for y in range(0, len(m)):
		for x in range(0, len(m[y])):
			if m[y][x] == '#':
				left += 1
				
	return left
				
	
cases = int(lines[0])
line = 0
for case in range(cases):
	line += 1
	data = lines[line].split()
	r = int(data[0])
	c = int(data[1])
	
	m = []
	for i in range(r):
		line += 1
		row = []
		for j in range(len(lines[line].strip())):
			row.append(lines[line][j])
		m.append(row)
		
	last = 99999999
	left = 99999998
	while left > 0 and left != last:
		last = left
		left = passover(m)
	
	of.write("Case #%d:\n" % (case + 1))
	if left == 0:
		for r in m:
			row = ''
			for c in r:
				row += c
		
			of.write(row + '\n')
	else:
		of.write('Impossible\n')
		
	
