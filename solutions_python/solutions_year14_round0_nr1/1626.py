inputfile = open('A-small-attempt0.in.txt')
outputfile = open('result.txt','w')


no_of_tests = int(inputfile.readline())


for t in range(no_of_tests):
	answer1 = int(inputfile.readline())
	cards1 = []
	for n in range(4):
		cards1.append(map(int,inputfile.readline().split()))
	answer2 = int(inputfile.readline())
	cards2 = []
	for n in range(4):
		cards2.append(map(int,inputfile.readline().split()))
	match = 0	
	card_no=-1
	for card1 in cards1[answer1-1]:
		for card2 in cards2[answer2-1]:
			if card1==card2:
				match+=1
				card_no = card1
				
	if match==0:
		print >>outputfile, "Case #%d: Volunteer cheated!" % (t+1)
	elif match==1:
		print >>outputfile, "Case #%d: %d" % (t+1,card_no)
	else:
		print >>outputfile, "Case #%d: Bad magician!" % (t+1)