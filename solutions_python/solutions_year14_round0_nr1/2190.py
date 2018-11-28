
for case_number in range(int(raw_input())):
	x = int(raw_input())
	x = set([map(int,raw_input().split()) for _ in range(4)][x-1])
	
	y = int(raw_input())
	y = set([map(int,raw_input().split()) for _ in range(4)][y-1])
	
	t = x & y
	
	print('Case #%d: %s' % (
		case_number + 1,
		'Volunteer cheated!' if not t else
		'Bad magician!' if len(t) > 1 else
		next(iter(t))
		))
	