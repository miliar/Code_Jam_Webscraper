import fileinput

i = 0

GABRIEL = 'GABRIEL'
RICHARD = 'RICHARD'

def solve(x,r,c):
	if x == 1:
		return GABRIEL
	if x >= 7:
		return RICHARD
	if r * c < x:
		return RICHARD

	if r + c < x + 1:
		return RICHARD

	if x == 2:
		if r * c % 2 == 0:
			return GABRIEL

	if x == 3:
		if r % 3 == 0 and c >= 2:
			return GABRIEL
		if c % 3 == 0 and r >= 2:
			return GABRIEL

	if x == 4:
		if r < 2 or c < 2:
			return RICHARD
		if r >= 3 and c % 4 == 0:
			return GABRIEL
		if c >= 3 and r % 4 == 0:
			return GABRIEL

	if x == 5:
		if r < 3 or c < 3:
			return RICHARD
		if r >= 3 and c % 5 == 0:
			return GABRIEL
		if c >= 3 and r % 5 == 0:
			return GABRIEL

	if x == 6:
		if r < 5 or c < 5:
			return RICHARD
		if r >= 3 and c % 6 == 0:
			return GABRIEL
		if c >= 3 and r % 6 == 0:
			return GABRIEL

	return RICHARD

if __name__ == '__main__':
	for line in fileinput.input():
		if i == 0:
			i += 1
			continue
		x, r, c = map(int,line.split(' '))
		print "Case #%d: %s" % (i, solve(x,r,c))
		i += 1
