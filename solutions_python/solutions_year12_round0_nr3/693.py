import string

f = open('C-large.in', 'r')
g = open('output.txt', 'w')



n = int(f.readline())
count = 1

while count <= n:
	line = f.readline()
	if '\n' in line:
		line = line[:-1]
	line = line.split()
	a = int(line[0])
	b = int(line[1])
	
	totalCount = 0
	numLen = len(str(a))
	
	counter = a
	while counter <= b:
		num = counter
		tempList = [num]
		for i in range(numLen - 1):
			num = ((num % 10) * 10**(numLen - 1)) + (num / 10)
			if num >= a and num <= b and num not in tempList:
				tempList.append(num)
				totalCount += 1
		counter += 1
		
	g.write("Case #" + str(count) + ": " + str(totalCount / 2) + '\n')

	count += 1
	
f.close()
g.close()