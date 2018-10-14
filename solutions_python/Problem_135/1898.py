from collections import Counter

def solve():
	rows = []
	for grid_id in range(2):
		answer_row = int(raw_input())
		for row in range(4):
			inp = raw_input();
			if row + 1 != answer_row:
				continue
			rows.append(map(int, inp.split(" ")))

	common = list((Counter(rows[0]) & Counter(rows[1])).elements())
	if len(common) == 0:
		return "Volunteer cheated!"
	elif len(common) == 1:
		return str(common[0])

	return "Bad magician!"

cases = int(raw_input())

for case_no in xrange(1, cases+1):
	print "Case #%d: %s" % (case_no, solve())
