def solve_line(line):
	found = False
	result = ''
	backlog = 0
	prev = ''
	for char in line:
		if char == '?':
			if found:
				result += prev
			else:
				backlog += 1
		else:
			if not found:
				found = True
				for i in xrange(backlog):
					result += char
			result += char
			prev = char
	return result

def solve():
	R, C = map(int, raw_input().strip().split())
	matrix = []
	previous_line = ''
	backlog = 0
	found = False
	for i in xrange(R):
		line = raw_input().strip()
		liner = ''
		if line.count('?') == C:
			if found:
				liner = previous_line
				print liner
			else:
				backlog += 1
				# store line in backlog
		else:
			liner = solve_line(line)
			if not found:
				found = True
				# solve for this line and copy upwards into backlog lines
				for i in xrange(backlog):
					print liner
			print liner
		previous_line = liner

for i in xrange(input()):
	print "Case #"+str(i+1)+':'
	solve()
