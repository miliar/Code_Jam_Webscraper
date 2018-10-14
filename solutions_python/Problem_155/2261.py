#f = open('A-small-practice.in')
f = open('ovationtest.txt')
n = int(f.readline())

for x in range(0, n):
	curLine = f.readline().split()
	sMax = int(curLine[0]) + 1
	string = curLine[1]

	i = 0
	sumPeople = 0

	for y in range(0, sMax):

		num = int(string[y])

		if sumPeople < y:
			i += 1
			sumPeople += 1

		sumPeople += num
		
	print("Case #" + str(x+1) + ": " + str(i))