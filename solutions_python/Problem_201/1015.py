from math import log
from math import pow

def binaryDiv(x):
	xd2 = x//2
	return int(x - xd2), int(xd2)

def solve(s):
	l = s.split(' ')
	n = int(l[0])
	k = int(l[1])
	beforeLevel = int(log(k, 2))
	numInBeforeLevels = pow(2, beforeLevel) - 1
	kLeft = k - numInBeforeLevels
	nLeft = n - numInBeforeLevels
	numIncurrentLevel = numInBeforeLevels + 1
	q = nLeft // numIncurrentLevel
	r = nLeft % numIncurrentLevel
	if 	kLeft <= r:
		choosedGap = q + 1
	else:
		choosedGap = q
	return '{} {}'.format(*binaryDiv(choosedGap - 1))
			
	
def getInputFromFile(filename):
	f = open(filename, 'rt')
	n = int(f.readline().rstrip())
	inputs = []
	for i in range(0, n):
		line = f.readline().rstrip()
		inputs.append(line)
	f.close()
	return n, inputs	
	
	
def getAns(filename, outputFile):
	n, inputs = getInputFromFile(filename)
	res = []
	for i in range(0, n):
		ans = solve(inputs[i])
		res.append('Case #{}: {}'.format(i+1, ans))
	f = open(outputFile, 'wt')
	s = '\n'.join(res) + '\n'
	print(s)
	f.write(s)
	f.close()
