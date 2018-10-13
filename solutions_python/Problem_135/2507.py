T = int(raw_input())

for i in range(1, T+1):
	
	answerToFirstQuestion = int(raw_input())
	
	firstArrangement = []
	secondArrangement = []
	
	for _ in xrange(4):
		firstArrangement.append([int(elem) for elem in raw_input().replace('\n', '').split(' ')])
	
	answerToSecondQuestion = int(raw_input())
	
	for _ in xrange(4):
		secondArrangement.append([int(elem) for elem in raw_input().replace('\n', '').split(' ')])
	
	posOne = set(firstArrangement[answerToFirstQuestion-1])
	posTwo = set(secondArrangement[answerToSecondQuestion-1])

	intersection = posOne.intersection(posTwo)
	length = len(intersection)

	if length == 1:
		solution = str(list(intersection)[0])
	if length > 1:
		solution = "Bad magician!"
	if length < 1:
		solution = "Volunteer cheated!"

	print "Case #"+str(i)+": " + solution