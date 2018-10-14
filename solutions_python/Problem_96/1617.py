for y in range(int(raw_input())):
	ints = map(int, raw_input().split())
	ng = ints[0]
	ns = ints[1]
	score = ints[2]
	score = 3*score
	scores = ints[3:]
	count = 0
	for z in range(ng):
		if (score - scores[z]) <= 2 and score/3 <= scores[z]:
			count = count + 1
		elif ns > 0:
			if score - scores[z] <= 4 and score/3 <= scores[z]:
				ns = ns - 1
				count = count + 1
	print 'Case #' + str(y+1) + ': ' + str(count)
