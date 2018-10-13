import sys
T = int(next(sys.stdin))

def read_grid(file):
	row = int(next(file))-1
	for i in range(4):
		line = next(file)
		if i==row:
			elements = set(map(int, line.split()))
	return elements

for x in range(T):
	solution = read_grid(sys.stdin) & read_grid(sys.stdin)
	if len(solution):
		if len(solution)==1:
			print("Case #%s: %s" % (x+1, solution.pop()))
		else:
			print("Case #%s: Bad magician!" % (x+1))
	else:
		print("Case #%s: Volunteer cheated!" % (x+1))

