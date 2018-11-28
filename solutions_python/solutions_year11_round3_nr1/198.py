import sys, itertools

def write_p(o, p):
	for i in p:
		for j in i:
			o.write(j)
		o.write('\n')
		
def no_blue(p, num_rows, num_cols):
	for i in range(0, num_rows):
		for j in range(0, num_cols):
			if p[i][j] == '#':
				return False
	return True
		
def blue_check(p, num_rows, num_cols):
	return True
	for i in range(0, num_rows):
		for j in range(0, num_cols):
			if i < num_rows - 1 and j < num_cols - 1:
				a = p[i+0][j+0] == '#'
				b = p[i+1][j+0] == '#'
				c = p[i+0][j+1] == '#' 
				d = p[i+1][j+1] == '#'
				aa = a and b and c and d
				bb = a == False and b == False and c == False and d == False
				if not aa or bb:
					return False
	return True
		


filename = sys.argv[1]
f = open(filename)
o = open(filename + ".out", "wt")
num_tests = int(f.readline())
for t in range(1, num_tests+1):
	o.write("Case #%d:\n" % t)

	num_rows, num_cols = [int(x) for x in f.readline().split()]
	p = []
	total = 0
	white = 0
	blue = 0
	for r in range(0,num_rows):
		c = f.readline().strip()
		total += len(c)
		for x in c:
			if x == '.': white += 1
			if x == '#': blue += 1
		p.append([x for x in c])
	#print p
	
	# check for easy cases
	if white == total:
		write_p(o,p)
	elif blue % 4 != 0:
		o.write("Impossible\n")
	else:
		for i in range(0, num_rows):
			for j in range(0, num_cols):
				blue_block = i < num_rows - 1 and j < num_cols -1 and p[i+0][j+0] == '#' and p[i+1][j+0] == '#' and p[i+0][j+1] == '#' and p[i+1][j+1] == '#'
				if blue_block:
					p[i+0][j+0] = '/'
					p[i+1][j+0] = '\\'
					p[i+0][j+1] = '\\'
					p[i+1][j+1] = '/'
		if no_blue(p, num_rows, num_cols):
			write_p(o,p)
		else:
			o.write("Impossible\n")
	
	#o.write("Case #%d: %s\n" % (t, res))
o.close()

