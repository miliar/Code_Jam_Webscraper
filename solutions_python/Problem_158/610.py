import sys

test = False

if(test):
	YES = 'YES'
	NO = 'NO'
else:
	YES = 'GABRIEL'
	NO = 'RICHARD'

def whichName(x, R, C):

	if(x > R and x > C):
		return NO
	
	if(x >= 7):
		return NO

	if((C == 1 or R == 1) and x >= 3):
		return NO

	if((C == 2 or R == 2) and x >= 4):
		return NO

	if ((R*C) % x != 0):
		return NO

	if ((R*C) % x == 0): 
		return YES

	else: raise('Error')
if __name__ == '__main__':

	if (len(sys.argv) < 2):
		test = True
		f = open('testc', 'r')

	else: 
		filename = sys.argv[1]
		f = open(filename, 'r')

	
	testCases = int(f.next())
	caseNum = 0

	for i in xrange(testCases):
		caseNum += 1
		l = f.next().split()

		
		x = int(l[0])
		R = int(l[1])
		C = int(l[2])
		
		name = whichName(x, R, C)

		if(test):
			print(l, 'Case #%s: %s' % (caseNum, name))
		else:
			print('Case #%s: %s' % (caseNum, name))
