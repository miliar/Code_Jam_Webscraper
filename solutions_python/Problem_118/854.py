def isPalindrome(i):
	s = str(i)
	l = len(s)
	for i in range(l/2):
		if s[i] != s[(l-1)-i]:
			return False
	return True

import math
f = open("input.txt")
o = open("output.txt", "w+")
for case in range(int(f.readline())):
	tot = 0
	if case % 100 == 0:
		print case
	lower, upper = [int(x) for x in f.readline().split()]
	lowerRoot = int(math.sqrt(lower))
	upperRoot = int(math.sqrt(upper))

	palin = "1"
	for i in range((len(str(lowerRoot))/2)-1):
		palin += '0'

	root = int(palin + palin[::-1])

	while root < lowerRoot:
		palin = str(int(palin) + 1)
		root = int(palin + palin[::-1])
	square = root*root
	while(square <= upper):
		
		if square >= lower and isPalindrome(square):
			tot += 1
		palin = str(int(palin) + 1)
		root = int(palin + palin[::-1])
		square = root*root

	palin = "1"
	for i in range((len(str(lowerRoot))/2)-1):
		palin += '0'

	root = int(palin + palin[-2::-1])

	while root < lowerRoot:
		palin = str(int(palin) + 1)
		root = int(palin + palin[-2::-1])
	square = root*root
	while(square <= upper):
		if square >= lower and isPalindrome(square):
			tot += 1
		palin = str(int(palin) + 1)
		root = int(palin + palin[-2::-1])
		square = root*root



	o.write("Case #" + str(case+1) + ": " + str(tot) + "\n")
o.close()

