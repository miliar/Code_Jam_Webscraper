import sys


def input_generator():
	for line in sys.stdin:
		for token in line[:-1].split(' '):
			if token != '' or token:
				yield token

myin = input_generator()

def get_row(n):
	res = None
	for r in range(4):
		row = [ int(myin.next()) for _ in range(4) ]
		if r == n:
			res = row
	return res

t = int(myin.next())
for c in range(1,t+1):
	g1 = int(myin.next()) - 1
	row1 = get_row(g1)
	g2 = int(myin.next()) - 1
	row2 = get_row(g2)
	cards = set(row1).intersection(set(row2))
	if len(cards) == 0:
		print "Case #%d: Volunteer cheated!" % (c,)
	elif len(cards) == 1:
		print "Case #%d: %d" % (c,cards.pop())
	else:
		print "Case #%d: Bad magician!" % (c,)

