t = int(raw_input())
tc = 1
while tc <= t:
	p = "Case #" + str(tc) + ": "
	tc = tc + 1
	r = int(raw_input())
	for i in range(1,5):
		line = raw_input()
		if i == r:
			a = set(line.split())
	s = int(raw_input())
	for i in range(1,5):
		line = raw_input()
		if i == s:
			b = set(line.split())
	a = a & b
	if len(a) == 1:
		for item in a:
			print p + str(item)
	if len(a) == 0:
		print p + "Volunteer cheated!"
	if len(a) > 1:
		print p + "Bad magician!"