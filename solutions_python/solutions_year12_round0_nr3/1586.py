#cycles a number by positions specified by digit
def cyclenumber(num, digit):
	partone = str(num)[-digit:]
	parttwo = str(num)[:len(str(num))-digit]
	return partone + parttwo

f = open('C-small-attempt0.in')

cases = int(f.readline())

for x in range(0,cases):
	
	total = 0
	
	pairs = []

	line = f.readline()
	args = line.split()
	
	low = int(args[0])
	high = int(args[1])

	for i in range(low,high+1):
		for j in range(1,len(str(i))):
			num = int(cyclenumber(i,j))
			numstr = str(num) + str(i)
			if (num >= low and num <= high and num < i and numstr not in pairs):
				total += 1
				pairs.append(numstr)

	print "Case #" + str(x+1) + ": " + str(total)
