import math

def readInput():
	f = open('C-small-attempt0.in', 'r')
	
	f.readline()
	
	intervals = []
	for line in f:
		if len(line.strip()) > 0:
			intervals.append([int(n) for n in line.strip().split()])

	return intervals

def isPalindrome(n):
	s = str(n)
	for i in range(0, (len(s) - 1) / 2 + 1):
		if s[i] != s[len(s) - i - 1]:
			return False
	return True

def processInterval(interval):
	min = int(math.ceil(math.sqrt(interval[0])))
	max = int(math.floor(math.sqrt(interval[1])))
	counter = 0
	for i in range(min, max + 1):
		if isPalindrome(i) and isPalindrome(i*i):
			counter = counter + 1
	return str(counter)

intervals = readInput()
results = []
i = 1
for interval in intervals:
	results.append('Case #' + str(i) + ': ' + processInterval(interval) + '\n')
	i = i + 1
	
# print reduce(lambda a,b: a + b, results)

f = open('C-small-attempt0.out', 'w')
f.writelines(results)
f.close()