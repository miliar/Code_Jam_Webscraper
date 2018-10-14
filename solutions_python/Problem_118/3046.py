import math
import sys
fIn = open('C-small.in.txt', 'r')
sys.stdout = open('C-small.out.txt', 'w')

tests = int(fIn.readline())

def palinCheck(n):
	num = str(int(n))
	leng = len(num)
	if leng == 1:
		palin = True
	elif num == num[::-1]:
		palin = True
	else:
		palin = False
	return palin

def sqrtCheck(n):
    return math.sqrt(n).is_integer()

for i in range(tests):
	output = 0
	ends = fIn.readline().split()
	for j in range(len(ends)):
		ends[j] = int(ends[j])
	for k in range(ends[0], ends[1]+1):
		root = math.sqrt(k)
		if palinCheck(k):
			if sqrtCheck(k):
				if palinCheck(root):
					output += 1
	print('Case #{0}: {1}').format(i+1, output)




