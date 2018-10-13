from sets import Set
n = int(raw_input())
for i in xrange(1,n+1):
	row = int(raw_input())
	list = Set([])
	counter = 0
	number = 0
	for j in xrange(0,4):
		a = raw_input()
		if (row == j+1):
			for s in a.split(' '):
				list.add(s)
	row = int(raw_input())
	for j in xrange(0,4):
		a = raw_input()
		if (row == j+1):
			for s in a.split(' '):
				if s in list:
					if counter == 1:
						print ("Case #" + str(i) + ": Bad magician!")
					counter += 1
					number = s
			if (counter == 1):
				print ("Case #" + str(i) + ": " + str(number))
			elif (counter == 0):
				print ("Case #" + str(i) + ": Volunteer cheated!")