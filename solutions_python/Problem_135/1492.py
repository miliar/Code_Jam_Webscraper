fout = open("output.txt",'w')
fout.write('')
fout.close()

fin = open('A-small.in')
N = int(fin.readline())

for i in range(N):
	ans1 = int(fin.readline())-1

	cards1 = []
	for line in range(4):
		row = fin.readline().split()
		row = map(int,row)
		cards1.append(row)

	ans2 = int(fin.readline())-1

	cards2 = []
	for line in range(4):
		row = fin.readline().split()
		row = map(int,row)
		cards2.append(row)

	p_cards = 0 #possible cards

	for c1 in cards1[ans1]:
		for c2 in cards2[ans2]:
			if c1 == c2:
				p_cards+=1
				chosen = c1

	fout = open("output.txt",'a')
	if p_cards == 0:
		fout.write('Case #%d: %s\n'%(i+1, 'Volunteer cheated!'))

	elif p_cards > 1: 
		fout.write('Case #%d: %s\n'%(i+1, 'Bad magician!'))

	else:
		fout.write('Case #%d: %d\n'%(i+1, chosen))

	fout.close()

fin.close





