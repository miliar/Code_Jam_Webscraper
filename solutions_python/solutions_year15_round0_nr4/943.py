def solve(s):
	x,r,c = map(int,s.split())
	if x >= 7:
		return "RICHARD"
	if (r*c)%x != 0:
		return "RICHARD"
	if x < 3:
		return "GABRIEL"
	if x == 3:
		if r >= 2 and c >= 2:
			return "GABRIEL"
		else:
			return "RICHARD"
	if x == 4:
		if r > 2 and c > 2:
			return "GABRIEL"
		else:
			return "RICHARD"
	if x == 5:
		if r > 3 and c > 3:
			return "GABRIEL"
		else:
			return "RICHARD"
	if x == 6:
		if r > 4 and c > 4:
			return "GABRIEL"
		else:
			return "RICHARD"

t = input()

for i in xrange(t):
	s = raw_input()
	print("Case #" + str(i+1) + ": " + str(solve(s)))