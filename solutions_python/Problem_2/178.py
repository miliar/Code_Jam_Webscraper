import sys, copy, datetime

f = open(sys.argv[1], 'r')
for i in range(int(f.readline())):
	T = datetime.timedelta(0, 0, 0, 0, int(f.readline().strip()))
	NA, NB = map(lambda x: int(x), f.readline().strip().split(' '))
	AB = {'start':[], 'stop':[]}
	BA = {'start':[], 'stop':[]}
	for j in range(NA):
		foo = map(lambda x: datetime.datetime.strptime(x, '%H:%M'), f.readline().strip().split(' '))
		AB['start'].append(foo[0])
		AB['stop'].append(foo[1])
	for j in range(NB):
		foo = map(lambda x: datetime.datetime.strptime(x, '%H:%M'), f.readline().strip().split(' '))
		BA['start'].append(foo[0])
		BA['stop'].append(foo[1])
	AB['start'].sort(); AB['stop'].sort(); BA['start'].sort(); BA['stop'].sort()
	deltafactor = 0
	for j in AB['start']:
		#print j
		#print filter(lambda x, j=j: x+T<=j, BA['stop'])
		try:
			BA['stop'].remove(filter(lambda x, j=j: x+T<=j, BA['stop'])[-1])
			NA -= 1
		except: pass
		#print 'BA left: ', BA['stop']
	for j in BA['start']:
		#print j
		#print filter(lambda x, j=j: x+T<=j, AB['stop'])
		try:
			AB['stop'].remove(filter(lambda x, j=j: x+T<=j, AB['stop'])[-1])
			NB -= 1
		except: pass
		#print 'AB left: ', AB['stop']
	#print (AB, BA, T)
	print 'Case #%d: %d %d'%(i+1, NA, NB)