import sys

fd = sys.stdin
outputFile = sys.stdout

def check(Li , Lo, T):
	result = 0
	for o in Lo:
		exist = False
		for i in Li:
			if (i+T) <= o:
				Li.remove(i)
				exist = True
				break
		if not exist:
			result += 1
				
	return result

def time(h, m):
	return int('%s%s'%(h,m))

def sortlist(l):
	l.sort(lambda x, y: x - y)
	return l

tests = int(fd.readline())

for test in xrange(0, tests):
	#print 'teste', test
	T = int(fd.readline())
	line = fd.readline()
	line = line.split(' ')
	AB = int(line[0])
	BA = int(line[1])
	NA = 0
	NB = 0
	A = {}
	A['in'] = []
	A['out'] = []
	B = {}
	B['in'] = []
	B['out'] = []

	for l in xrange(0, AB):
		line = fd.readline()
		line = line.split(' ')
		out = line[0].split(':')
		inn = line[1].split(':')
		timeo = time(out[0],out[1]) 
		timei = time(inn[0], inn[1])
		A['out'].append(timeo)
		B['in'].append(timei)

	for l in xrange(0, BA):		
		line = fd.readline()
		line = line.split(' ')
		out = line[0].split(':')
		inn = line[1].split(':')
		timeo = time(out[0],out[1]) 
		timei = time(inn[0], inn[1])
		B['out'].append(timeo)
		A['in'].append(timei)

	A['in']=sortlist(A['in'])
	A['out']=sortlist(A['out'])
	B['in']=sortlist(B['in'])
	B['out']=sortlist(B['out'])	

	NA = check(A['in'], A['out'], T)
	NB = check(B['in'], B['out'], T)

	outputFile.write('Case #%d: %d %d\n'% (test+1, NA, NB))
