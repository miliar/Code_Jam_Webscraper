''' first quals problem '''

T = int(raw_input())
for x in range(T):
	answerA = int(raw_input())
	A = raw_input().split()
	B = raw_input().split()
	C = raw_input().split()
	D = raw_input().split()
	
	answerB = int(raw_input())
	cA = raw_input().split()
	cB = raw_input().split()
	cC = raw_input().split()
	cD = raw_input().split()
	
	if answerA == 1:
		myRow = A
	elif answerA == 2:
		myRow = B
	elif answerA == 3:
		myRow = C
	else:
		myRow = D
	
	if answerB == 1:
		myCol = cA
	elif answerB == 2:
		myCol = cB
	elif answerB == 3:
		myCol = cC
	else:
		myCol = cD	
	
	count = 0
	for i in range(4):
		for j in range(4):
			if myRow[i] == myCol[j]:
				count = count+1
				myVal = myRow[i]	
	if count == 1:
		answer = myVal
	elif count == 0:
		answer = "Volunteer cheated!"
	else:
		answer = "Bad magician!"
			
	print "Case #"+str(x+1)+": "+answer
