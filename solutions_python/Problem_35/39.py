from __future__ import with_statement

def process_case(data, out):
    
    def propagate(x, y, b = None, previous = None):
	if previous == None:
	    previous = []
	if basin[y][x]:
	    b = basin[y][x]
	    for x, y in previous:
	        basin[y][x] = b
	    return
	ans = geo[y][x]
	dir = 'sink'
	if y > 0:
	    n = geo[y-1][x]
	    if n < ans:
		ans, dir = n, 'n'
	if x > 0:
	    west = geo[y][x-1]
	    if west < ans:
		ans, dir = west, 'w'
	if x < w - 1:
	    e = geo[y][x+1]
	    if e < ans:
		ans, dir = e, 'e'
	if y < h - 1:
	    s = geo[y+1][x]
	    if s < ans:
		dir = 's'
	
	previous.append((x, y))
	
	if dir == 'n':
	    propagate(x, y-1, b, previous)
	elif dir == 'w':
	    propagate(x-1, y, b, previous)
	elif dir == 'e':
	    propagate(x+1, y, b, previous)
	elif dir == 's':
	    propagate(x, y+1, b, previous)
	elif dir == 'sink':
	    if basin[y][x]:
		b = basin[y][x]
	    else:
		b = basins.pop()
	    for x, y in previous:
	        basin[y][x] = b

    h, w = map(int, data.readline().strip("\n").split(" "))
    geo = []
    basin = []
    basins = list('abcdefghijklmnopqrstuvwxyz'[::-1])
    for i in range(h):
	geo.append(map(int, data.readline().strip("\n").split(" ")))
	basin.append(map(lambda x: 0, geo[-1]))
    for y in range(h):
	for x in range(w):
	    if not basin[y][x]:
		propagate(x, y)#, basin[y][x])
    out.write('\n'.join((' '.join(x for x in row) for row in basin)))

def process_file(fname):    
    
    with open(fname, "r") as data:
	with open("answer_" + fname, "w") as answer:
	    n = int(data.readline().strip("\n"))
	    for i in range(n):
		answer.write("Case #%d:\n" % (i+1))
		process_case(data, answer)
		answer.write("\n")
process_file("B-large.in")