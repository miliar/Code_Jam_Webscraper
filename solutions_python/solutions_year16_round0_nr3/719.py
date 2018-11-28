outfile = open("C-outputA.out", "w")
outfile.write("Case #1:\n")

def toBinary(n):
	if n < 2:
		return str(n)
	return toBinary(n//2) + str(n%2)

def toBase(n, base):
	total = 0
	for character in range(0, len(n)):
		total += int(n[character])*(base**(len(n)-character-1))
	return total

def lowestFactor(number):
	i = 2
	while i < 1000000:
		if number % i == 0:
			return i
		i += 1
	return False


solutions = {}
for i in range(2147483649, 4294967296, 2):
	print(toBinary(i))
	if len(solutions) == 500:
		break
	binaryNum = toBinary(i)
	factors = []
	for j in range(2, 11):
		temp = toBase(binaryNum, j)
		#print("{0} = {1} in base {2} = {3}".format(i, binaryNum, j, temp))
		factor = lowestFactor(temp)
		factors.append(factor)
		if not factor:
			break
	else:
		solutions[binaryNum] = factors
		print(len(solutions))
		outfile.write("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}\n".format(binaryNum, factors[0], factors[1], factors[2], factors[3], factors[4], factors[5], factors[6], factors[7], factors[8]))

#print(solutions)

outfile.close()