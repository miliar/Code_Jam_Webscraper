in_file = open('/home/kyeshi_0913/Downloads/A-small-attempt0.in').read()

lines = in_file.split('\n')
t = int(lines[0])
del lines[0]

for case in range(t): # Loop per case
	ans = []
	for q in range(2): # Loop per question
		ans.append([int(i) for i in lines[int(lines[0])].split(' ')])
		del lines[:5]

	# Compare answers, find overlap
	overlap = []
	for n in ans[0]:
		if n in ans[1]: overlap.append(n)

	if len(overlap) > 1: msg = 'Bad magician!'
	elif len(overlap) < 1: msg = 'Volunteer cheated!'
	else: msg = str(overlap[0])

	print('Case #%d: %s' % (case+1, msg))










