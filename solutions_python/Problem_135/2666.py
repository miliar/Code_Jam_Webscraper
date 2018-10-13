import sys

def read_answer(f):
	line_no = int(f.readline().strip())
	lines = [f.readline() for i in range(4)]
	line = set(map(int, lines[line_no - 1].split()))
	return line

with open(sys.argv[1], 'r') as f:
	cases = int(f.readline().strip())
	for case in range(cases):
		a1 = read_answer(f)
		a2 = read_answer(f)
		cards = a1 & a2
		if len(cards) < 1:
			result = 'Volunteer cheated!'
		elif len(cards) > 1:
			result = 'Bad magician!'
		else:
			card, = cards
			result = str(card)
		print('Case #%d: %s' % (case + 1, result))

