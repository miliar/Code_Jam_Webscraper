import fileinput
import sys


def is_there_a_recycled_pair(a,b,numberOfDigits):
	tempstr = str(a)
	for i in range(numberOfDigits):
		tempstr = tempstr[-1] + tempstr[:-1]
		if int(tempstr) == b:
			return True
	return False


i = 1
firstone = True
for line in fileinput.input():
	if firstone:
		firstone = False
		continue

	sys.stdout.write("Case #" + str(i) + ": ")
	AandB = line.split(' ')
	A = int(AandB[0])
	B = int(AandB[1])
	count = 0

	numberOfDigits = len(AandB[0])

	# for each number equal to or less than B (called m) (going up)
	for m in range(A+1,B+1):
		# for each number equal to greater than A but less than m (called n) (going up)
		for n in range(A, m):
			# see if n can be rearranged to get m
				if (is_there_a_recycled_pair(n,m,numberOfDigits)):
					# if so, increment the count
					count += 1
				#sys.stdout.write(tup[1])
				#break
	sys.stdout.write(str(count) + '\n')
	i+=1
