def TidyNumber(num):
	num = str(num)

	for i in xrange(0,len(num)-1):
		if (num[i] <= num[i+1]):
			continue
		else:
			return False
	return True

def GenerateNumbers(num):
	temp = num - 1
	while (temp >= 0):
		yield temp
		temp = temp - 1

f = open("B-small-attempt1.in",'r')
f1 = open("output.out", "a")

numberOfCases = int(f.readline())
inputs = []

for i in xrange(1,numberOfCases+1):
	inputs.append(int(f.readline()))

for i in inputs:
	temp = i
	gen = GenerateNumbers(temp)

	while TidyNumber(temp) == False:
		temp = next(gen)
	f1.write("Case #" + str((inputs.index(i))+1) + ": " + str(temp) + "\n")

