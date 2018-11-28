from sets import Set

filename = raw_input('Enter a file name: ')

with open(filename) as fp:
    content = fp.read().splitlines()

testCases = content.pop(0)


for x in range(0, int(testCases)):
	firstAnswer = content[0]
	set1 = content[int(firstAnswer)].split()

	for y in range(0, 5):
		content.pop(0)
	
	secondAnswer = content[0]
	set2 = content[int(secondAnswer)].split()
	
	for z in range(0, 5):
		content.pop(0)
	
	intersect = list(set(set1) & set(set2))
	
	if len(intersect) == 0:
		answer = "Volunteer cheated!"
	elif len(intersect) == 1:
		answer = str(intersect[0])
	else:
		answer = "Bad magician!"
	
	print "{}{}{}{}".format("Case #", x+1,": ", answer)