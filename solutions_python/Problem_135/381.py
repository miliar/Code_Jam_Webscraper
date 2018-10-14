t = int(input())
for testcase in range(1,t+1):
	rows = []
	r1 = int(input())
	for i in range(1,5):
		r = list(map(int,input().split()))
		if i == r1:
			row1 = r

	r2 = int(input())
	for i in range(1,5):
		r = list(map(int,input().split()))
		if i == r2:
			row2 = r
	cards = 0
	cardnum = -1
	for i in row1:
		if i in row2:
			cards+=1
			cardnum = i
	if cards==0:
		print ("Case #" + str(testcase) + ": Volunteer cheated!")
	elif cards==1:
		print ("Case #" + str(testcase) + ": " + str(cardnum))
	else:
		print ("Case #" + str(testcase) + ": Bad magician!")

