def find_last(line):
	last = 0
	line = line[0]
	for i in xrange(len(line)):
		if(line[i] == '1'):
			last = i
	return last

def matches_to_line	(line, i):
	return (find_last(line) < i+1)
	
def swap(mat, i, j, size):
	tmp = mat[j]
	for k in range(j, i, -1):
		mat[k] = mat[k-1]
	mat[i] = tmp
	return mat
			
def solve_case(mat, size):
	swaps = 0;
	for i in xrange(size):
		last = find_last(mat[i])
		if(last <= i):
			continue;
		else:
			for j in xrange(size):
				if(j > i and matches_to_line(mat[j], i)):
					mat = swap(mat, i, j, size)
					swaps += j-i
					break
	return swaps


file = open("c:\\input.txt")
cases = int(file.readline())
for i in xrange(cases):
	lines = int(file.readline())
	mat = []
	for j in xrange(lines):
		mat.append(file.readline().split())
	print "Case #%d: %d" %(i+1, solve_case(mat, lines))
