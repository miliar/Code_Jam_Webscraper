import sys
inp = open("in.txt")
out = open("out.txt","w+")
sys.stdout = out

t = int(inp.readline())

def print_case(case, result):
	print "Case #%d: %s" % (case, str(result))

def parse_matrix():
	m = []
	for i in xrange(4):
		m.append([int(x) for x in inp.readline().split()])
	return m

for tc in xrange(t):
	r1 = int(inp.readline()) - 1
	m1 = parse_matrix()
	r2 = int(inp.readline()) - 1
	m2 = parse_matrix()
	result = set(m1[r1]).intersection(m2[r2])
	if len(result) == 0:
		y = "Volunteer cheated!"
	elif len(result) > 1:
		y = "Bad magician!"
	else:
		y = list(result)[0]
	print_case(tc+1, y)
