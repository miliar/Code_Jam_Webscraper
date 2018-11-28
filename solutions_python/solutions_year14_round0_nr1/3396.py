
testCases= raw_input()

for i in range(1,int(testCases)+1):
	Row = int(raw_input())
	#print  "First Row = " + str(Row)
	cards =[]
	cards.append(raw_input())
	cards = cards + [raw_input()]
	cards = cards + [raw_input()]
	cards = cards + [raw_input()]

	cardRowOne = cards[Row-1]
	
	Row = int(raw_input())
	cards =[]
	cards.append(raw_input())
	cards = cards + [raw_input()]
	cards = cards + [raw_input()]
	cards = cards + [raw_input()]
	
	cardRowTwo = cards[Row-1]
	
	#print "The first row contains these cards : " + cardRowOne
	#print "The second row contains these cards : " + cardRowTwo
	
	rowOne = []
	rowTwo = []
	for x in cardRowOne.split(" "):
		rowOne.append(int(x))
		
	for x in cardRowTwo.split(" "):
		rowTwo.append(int(x))
	
	#print rowOne
	#print rowTwo
	
	matches = 0
	
	for b in rowOne:
		if b in rowTwo:
				matches+=1
				match = b
				
	if matches == 1:
		print "Case #" + str(i) + ": " + str(match)
	elif matches == 0:
		print "Case #" + str(i) + ": " + "Volunteer cheated!"
	elif matches > 1:
		print "Case #" + str(i) + ": " + "Bad magician!"
	

	
	
	

