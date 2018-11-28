n = int(raw_input())
for case in range(1, n + 1):
	counts = [0] * 17
	for vol in range(2):
		t_row = int(raw_input())
		for num_line in range(1, 5):
			row = raw_input()
			if num_line == t_row:
				for x in row.strip().split(' '):
					counts[int(x)] += 1
	answer = "Volunteer cheated!"
	for i in range(len(counts)):
		if counts[i] > 1:
			if answer != "Volunteer cheated!":
				answer = "Bad magician!"
				break
			answer = str(i)
	print "Case #%d: %s" % (case, answer)
