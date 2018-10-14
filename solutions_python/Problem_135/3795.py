f = open('A-small-attempt1.in','r')
T = int(f.readline())
for t in range(T):
	row = int(f.readline())
	cards = []
	for r in range(4):
		cards.append(f.readline().split())
	row1 = cards[row-1]
	cards = []

	row = int(f.readline())
	for r in range(4):
		cards.append(f.readline().split())
	row2 = cards[row-1]

	answer = set(row1).intersection(set(row2))
	if len(answer)==1:
		print "Case #%d: %d"%(t+1,int(answer.pop()))
	elif len(answer)==0:
		print "Case #%d: Volunteer cheated!"%(t+1)
	else:
		print "Case #%d: Bad magician!"%(t+1)