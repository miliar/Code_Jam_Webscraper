import math

def twice(liste):
	m = 0
	m2 = 0
	for i in liste:
		if i > m:
			m2 = m
			m = i
		elif i > m2:
			m2 = i
	return m2

def eat(pancakes):
	for i in range(0, len(pancakes)):
		pancakes[i] = max(pancakes[i] - 1, 0)
	return pancakes

def numBiggerThan(pancakes, number):
	count = 0
	for i in pancakes:
		if i > number:
			count += 1
	return count

def solve(testers, pancakes):
	print pancakes, "needs"
	rounds = 0
	while (sum(pancakes) > 0):
		rounds += 1
		most = max(pancakes)
		if (most == 9 and 3 > numBiggerThan(pancakes, 3)):
			ind = pancakes.index(most)
			pancakes[ind] = most / 3.0
			pancakes.append(2 * (most / 3.0))
			#print "Thirded", most, "into", math.floor(most / 2.0), "and", math.ceil(most / 2.0)
		elif (most / 2) >= numBiggerThan(pancakes, most / 2):
			ind = pancakes.index(most)
			pancakes[ind] = math.floor(most / 2.0)
			pancakes.append(math.ceil(most / 2.0))
			#print "Split", most, "into", math.floor(most / 2.0), "and", math.ceil(most / 2.0)
		else:
			eat(pancakes)
			#print "eat", pancakes
	return str(rounds)


name = "B-small-attempt3"
fi = open(name + ".in", "r")

fout = open(name + ".out", "w")

numTestCases = int(fi.readline())
print "#TestCases: ", numTestCases

for i in range(0, numTestCases):
	line = int(fi.readline().strip())
	line2 = fi.readline().strip().split(" ")
	line2 = map(int, line2)

	fout.write("Case #" + str(i + 1) + ": " + solve(line, line2) + "\n")
	#print "Case #" + str(i + 1) + ": " + solve(line, line2)

fi.close()
fout.close()