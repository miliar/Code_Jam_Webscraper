for n in range(input()):
	first_answer = input()
	first_puzzle = []
	for i in range(4):
		first_puzzle.append(raw_input().split())
	second_answer = input()
	second_puzzle = []
	for i in range(4):
		second_puzzle.append(raw_input().split())
	a = first_puzzle[first_answer-1]
	b = second_puzzle[second_answer-1]
	c = []
	for i in a:
		if i in b:
			c.append(i)

	if len(c) == 1:
		print 'Case #%d: %s' %(n+1, c[0])
	elif len(c) == 0:
		print 'Case #%d: Volunteer cheated!' %(n+1)
	else:
		print 'Case #%d: Bad magician!' %(n+1)