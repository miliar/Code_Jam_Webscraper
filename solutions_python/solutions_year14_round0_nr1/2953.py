T = input()

for t in range(1, T+1):
	posans = set([])
	line1 = input()
	for linenum in range(1, 5):
		line = raw_input().split()
		if linenum == line1:
			posans = set(line)
	
	line2 = input()
	for linenum in range(1, 5):
		line = raw_input().split()
		if linenum == line2:
			posans.intersection_update(set(line))
	ans = ""
	if len(posans) == 0:
		ans = "Volunteer cheated!"
	elif len(posans) > 1:
		ans = "Bad magician!"
	else:
		ans = posans.pop()
	
	print "Case #%d: %s" % ( t, ans )
