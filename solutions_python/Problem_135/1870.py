from sets import Set

n = int(raw_input())

for i in xrange(0,n):

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

						print ("Case #2: Bad magician!")

					counter += 1

					number = s

			if (counter == 1):

				print ("Case #1: " + str(number))

			elif (counter == 0):

				print ("Case #3: Volunteer cheated!")