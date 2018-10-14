import sys
import itertools

def int2bin(n):
	bStr = ''
	if n < 0:  raise ValueError, "must be a positive integer"
	if n == 0: return '0'
	while n > 0:
		bStr = str(n % 2) + bStr
		n = n >> 1
	return bStr

def binaryAdd(x, y):
	sx = int2bin(x)
	sy = int2bin(y)
	
	if len(sx) > len(sy):
		sy = sy.rjust(len(sx),'0')
	else:
		sx = sx.rjust(len(sy),'0')

	result = ''
	for i in range(0,len(sx)):
		if sx[i] == sy[i]:
			result = result + '0'
		else:
			result = result + '1'

	return int(result,2)

def solve(line):
	max = -1
	indexes = range(len(line))
	for i in range(1, len(indexes)):
		c = itertools.combinations(indexes,i)
		for x in c:
			seanList = []
			patList = []
			for j in range(len(line)):
				if j in x:
					seanList.append(line[j])
				else:
					patList.append(line[j])
			
			seanSum = reduce(binaryAdd, seanList)
			patSum = reduce(binaryAdd, patList)
			
			if seanSum == patSum:
				seanSum = sum(seanList)
				if seanSum > max:
					max = seanSum
			
	if max == -1:
		return "NO"
	else:
		return str(max)
		
i = 0
for line in open(sys.argv[1]):  
	if i > 0 and i%2==0:
		tmp = solve(map(int,line.strip().split()))
		print "Case #%s: %s" %(i/2, "".join(tmp))
	i += 1
    