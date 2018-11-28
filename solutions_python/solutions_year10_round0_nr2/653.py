import sys
import math
def main():
	inputFile = open(sys.argv[1])
	c = int(inputFile.readline())
	
	for i in range(c):
		input = inputFile.readline().split(' ')
		input.pop(0)
		for j in range(len(input)):
			input[j] = int(input[j])
		input = list(set(input))
		input.sort()
		diffs = []
		last = 0
		for j in range(len(input)):
			diffs.append(input[j]-last)
			last = input[j]
		diffs.pop(0)
		t = getT(diffs[0], diffs[1:])
		
		if divmod(input[0], t)[1] is 0:
			n = input[0] / t
		else:
			n = input[0] / t + 1
		y = n*t - input[0]
		while not yTrue(y, input, t):
			n += 1
			y = n*t - input[0]
		print "Case #{0}: {1}".format(i+1, y)
			
	inputFile.close()
	return 0

def yTrue(y, numbers, t):
	for x in numbers:
		if divmod(x+y, t)[1] > 0:
			return False
	return True

def getT(t, diffs):
	for i in range(len(diffs)):
		if divmod(diffs[i], t) > 0:
			t = getT(stein(t, diffs[i]), diffs[i+1:])
			break
	return t

def stein(a, b):
	k = 0
	while (a & 1) is 0 and (b & 1) is 0:
		a = a/2
		b = b/2
		k = k+1 
	if (a & 1) is 0:
		t = -b
	else:
		t = a
	while t is not 0:
		while (t & 1) is 0:
			t = t/2
		if t > 0:
			a = t
		else:
			b = -t
		t = a - b
	return a * pow(2, k)

if __name__ == '__main__':
	main()
