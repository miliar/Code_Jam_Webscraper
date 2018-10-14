def sol(cse):
	r1 = input()
	a = []
	for i in range(0,4):
		if i == r1-1:
			a = map(int, raw_input().split())
		else:
			raw_input()
	r2 = input()
	b = []
	for i in range(0,4):
		if i == r2-1:
			b = map(int, raw_input().split())
		else:
			raw_input()
	c = [x for x in a if x in b]
	if len(c) == 1:
		print("Case #%d: %d" % (cse, c[0]))
	elif len(c) == 0:
		print("Case #%d: Volunteer cheated!" % (cse))
	else:
		print("Case #%d: Bad magician!" % (cse))




n = input()
for i in range(1, n+1):
	sol(i)