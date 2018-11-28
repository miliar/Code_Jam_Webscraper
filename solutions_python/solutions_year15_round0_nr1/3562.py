inputFile = open('input','r')
outputFile = open('result','r+')
total_test_case = int(inputFile.readline())
current_case = 1
counter = 0
friend_needed = 0
for line in inputFile:
	splited = []
	for x in line:
		if x != ' ' and x != '\n':
			splited += [x]
	maxShy = int(splited[0])
	splited = splited[1:]
	try:
		index_first_zero = splited.index('0')
	except ValueError:
		pass
	for x in range(0,len(splited)):
		if counter < x and splited[x] != '0':
			friend_needed += x - counter
			counter += x - counter
		counter += int(splited[x])
	outputFile.write('Case #' + str(current_case) + ': ' + str(friend_needed) + '\n')
	current_case += 1
	counter = 0
	friend_needed = 0


