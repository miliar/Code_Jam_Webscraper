def get_answer(x, r, c):
	if x == 1:
		return "GABRIEL"
	if r*c < x:
		return "RICHARD"
	grid = (min(r,c), max(r,c))
	if grid == (1,1) or grid == (1,3):
		return "RICHARD"
	if grid == (1,2) or grid == (1,4) or grid == (2,4) or grid == (2,2):
		if x == 2:
			return "GABRIEL"
		else:
			return "RICHARD"
	if grid == (2,3):
		if x in [2,3]:
			return "GABRIEL"
		else:
			return "RICHARD"
	if grid == (4,4):
		if x in [2,4]:
			return "GABRIEL"
		else:
			return "RICHARD"
	if grid == (3,4):
		return "GABRIEL"
	if grid == (3,3):
		if x == 3:
			return "GABRIEL"
		else:
			return "RICHARD"
	
	return "FAIL"


t = int(raw_input(""))
for t_ in range(1,t+1):
	x, r, c = raw_input("").split(" ")
	r = int(r)
	x = int(x)
	c = int(c)
	print "Case #%s: %s" % (t_, get_answer(x,r,c))
