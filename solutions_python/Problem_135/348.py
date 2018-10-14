#!/usr/local/bin/env python
inFile = open("A-small-attempt0.in.txt")
numbers = int(inFile.readline())
c = 1
results = ""
while c <= numbers:
	r = ''
	firstAnswer = int(inFile.readline())
	numbers1 = str()
	for i in range(4):
		if i == firstAnswer-1:
			numbers1 = inFile.readline()
		else:
			inFile.readline()
	if numbers1[len(numbers1)-1] == '\n':
		numbers1 = numbers1[0:len(numbers1)-1]
	numbers2 = str()
	secondAnswer = int(inFile.readline())
	for i in range(4):
		if i == secondAnswer - 1:
			numbers2 = inFile.readline()
		else:
			inFile.readline()
	if numbers2[len(numbers2)-1] == '\n':
		numbers2 = numbers2[0:len(numbers2)-1]

	number1Set = set(numbers1.split(' '))
	number2Set = set(numbers2.split(' '))
	if len(number1Set.intersection(number2Set)) == 0:
		r = 'Volunteer cheated!'
	elif len(number1Set.intersection(number2Set)) == 1:
		r = str(number1Set.intersection(number2Set).pop())
	else:
		r = 'Bad magician!'
	results += "Case #" + str(c) + ": " + r + '\n'
	c += 1
outFile = open("A-small-practice.out.txt", 'w')
outFile.write(results)