inputdata = """INPUT"""

def chunks(l, n):
	for i in xrange(0, len(l), n):
		yield l[i:i+n]

allLines = inputdata.split('\n')

for ct, lines in enumerate(chunks(allLines, 10)):
	firstindex = lines[0]
	options = lines[int(firstindex)].split(' ')
	secondIndex = lines[5]
	secondoptions = lines[int(secondIndex)+5].split(' ')

	answeredAlready = False
	answer = 'Volunteer cheated!'

	for i in options:
		try:
			secondoptions.index(i)
			if answeredAlready:
				answer = 'Bad magician!'
			else:
				answer = i
				answeredAlready = True
		except ValueError:
			continue

	print 'Case #{}: {}'.format(ct+1, answer)
