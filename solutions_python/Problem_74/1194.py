# sluttFil = open('losning.txt', 'w')
# innFil = open('A-small.in', 'r')

linjer = []
fil = open('A-large.in','r')


for line in fil:
	linjer.append(line)
linjer.pop(0) 

fil.close()


casenumber = 1
fil = open('A-output-large.txt','w')

for testStreng in linjer:
	i = 0

	nestenummer = ""
	while testStreng[i] != ' ':
		nestenummer += testStreng[i]
		i+=1	



	N = int(nestenummer)
	print testStreng

	testStreng = str(testStreng[i+1:])
	testStreng = testStreng.strip()

	

	orange = []
	blue = []
	order = ""

	for num in range(N):
		testStreng.strip()
		i = 0

	
		if testStreng[0] == 'O':
			nestenummer = ""
			while len(testStreng)>i+2 and testStreng[i+2] != ' ':
				nestenummer += testStreng[i+2]
				i+=1				
			print "- nummer: ",nestenummer
			orange.append(int(nestenummer))
			order = order + "o"

		else:
			nestenummer = ""
			while len(testStreng)>i+2 and testStreng[i+2] != ' ':
				nestenummer += testStreng[i+2]
				i+=1
			print "- nummer: ",nestenummer
			blue.append(int(nestenummer))
			
			order = order + "b"
		testStreng = testStreng[3+i:]

	print order
	print 'Orange:'
	print orange
	

	print 'Blue:'
	print blue

	


	print '\n Starting tests: \n'

	bluePos = 1
	orangePos = 1

	counter = 0

	while order:
		pressed = False

		# Blue
		# print 'blueMove: ', bluePos, '\t orangeMove: ', orangePos

		if blue:
			if bluePos < blue[0]:
				bluePos += 1	
			elif bluePos > blue[0]:
				bluePos -= 1	
			else:
				if order[0] == "b":
					order = order[1:]
					blue.pop(0)
					pressed = True
					#print '- Blue press -'
			
	
		# Orange
		if orange:
			if orangePos < orange[0]:
				orangePos += 1	
			elif orangePos > orange[0]:
				orangePos -= 1	
			else:
				if order[0] == "o" and not pressed:
					order = order[1:]
					orange.pop(0)
					#print '- Orange press -'
		
		
		counter += 1
	print "Counter: ", counter

	fil.write("Case #"+str(casenumber)+": "+str(counter)+"\n")

	casenumber +=1
	



fil.close()
print '\n Mission sucessful, but the cake is a lie'


