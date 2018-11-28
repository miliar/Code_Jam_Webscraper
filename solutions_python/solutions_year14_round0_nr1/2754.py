import sys

def parse_arrangement(f):
	row = int(f.readline()) - 1
	return set([
		map(int, f.readline().strip().split())
		for i in range(4)
	][row])

with open(sys.argv[1]) as f:
	for case in range(int(f.readline())):
		row1 = parse_arrangement(f)
		row2 = parse_arrangement(f)
		intersection = row1.intersection(row2)
		if not intersection:
			answer = 'Volunteer cheated!'
		elif len(intersection) > 1:
			answer = 'Bad magician!'
		else:
			answer = intersection.pop()
		print 'Case #%s: %s' % (case + 1, answer)