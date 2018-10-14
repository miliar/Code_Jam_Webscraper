with open('input.txt') as inpt:
	lines = inpt.readlines()
	tests = int(lines[0])
	cheat = 'Volunteer cheated!'
	bad = 'Bad magician!'
	with open('output.txt','w') as out:
		for i in xrange(tests):
			choice1 = int(lines[i*10 + 1])
			cards1 = lines[i*10 + choice1 + 1]
			choice2 = int(lines[i*10 + 6])
			cards2 = lines[i*10 + choice2 + 6]			
			cards = cards1.split()
			match = False
			multiple_match = False
			for card in cards:
				if card in cards2.split(): 
					if not match:
						matched_card = card
						match = True
					else:
						multiple_match = True
			if multiple_match:
				print >> out, 'Case #%d:' % (i+1), bad
			elif match:
				print >> out, 'Case #%d:' % (i+1), matched_card
			else:
				print >> out, 'Case #%d:' % (i+1), cheat

		