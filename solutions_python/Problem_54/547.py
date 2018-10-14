import sys

def FairWarning(filename):
	file = open(filename, 'r')
	c = file.readline()
	
	try:
		i = 1
		for line in file:
			list = line.split(' ')
			params = []
			for n in range(1, len(list)):
				v = int(list[n])
				#params.append(int(list[n]))
				try:
					params.index(v)
				except ValueError:
					params.append(v)
				
			print 'Case #%d: %d'%(i,GetT(params))
			i += 1
	finally:
		file.close()

def GetT(params):
	params.sort()
	min = params[0]
	T = params[len(params) - 1]
	last_GCD = 0
	for n in range(0, len(params) - 1):
		result = abs(params[n] - params[n+1])
		last_GCD = GetGCD(last_GCD, result)
	#print 'GCD', last_GCD
	if min % last_GCD == 0:
		return 0
	else:
		return last_GCD - min % last_GCD
	
def GetGCD(a, b):
	if b > 0:
		return GetGCD(b, a % b)
	return a

if __name__ == '__main__':
	#print sys.argv[1]
    FairWarning(sys.argv[1])