import sys
from collections import Counter

BAD = 'Bad Magician!'
CHEATED = 'Volunteer cheated!'

T = int(sys.stdin.readline())

for case in range(1, T+1):
	first_choice = int(sys.stdin.readline()) - 1
	first_rows = [
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split()
	]
	second_choice = int(sys.stdin.readline()) - 1
	second_rows = [
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split(),
		sys.stdin.readline().split()
	]
	possibles = Counter(first_rows[first_choice])
	location = Counter(second_rows[second_choice])

	result = [x for x, y in Counter(possibles + location).items() if y > 1]
	
	if len(result) == 0:
		text = CHEATED
	elif len(result) > 1:
		text = BAD
	else:
		text = str(result[0])
	
	sys.stdout.write('Case #%d: %s\n' % (case, text))

