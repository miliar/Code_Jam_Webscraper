
r = open("A-small-attempt0.in", 'r')
w = open("A-small.out", 'w')

n = int(r.readline()) # num cases

def checkConsec(chars):
	c = chars[0]

	if c != '.':
		for i in range(1,4):
			if chars[i] != c and (chars[i] != 'T'):
				return '.'

	if c == 'T':
		c = chars[3]

	return c

def checkHorizontal(brd):
	for i in range(0, 13, 4):
		c = checkConsec([brd[i], brd[i+1], brd[i+2], brd[i+3]])
		if c != '.':
			return c

	return '.'

def checkVertical(brd):
	for i in range(4):
		c = checkConsec([brd[i], brd[i+4], brd[i+8], brd[i+12]])
		if c != '.':
			return c

	return '.'

for tc in range(n):
	brd = ""
	for i in range (4):
		brd += r.readline().strip()
	r.readline()

	w.write("Case #"+str(tc+1)+": ")

	c = checkConsec([brd[0], brd[5], brd[10], brd[15]])
	if c == '.':
		c = checkConsec([brd[3], brd[6], brd[9], brd[12]]) 
		if c == '.':
			c = checkHorizontal(brd)
			if c == '.':
				c = checkVertical(brd)

	if c == '.':
		if brd.find(".") > -1:
			w.write("Game has not completed")
		else:
			w.write("Draw")
	else:
		w.write(c+" won")

	w.write("\n")

r.close()
w.close()
