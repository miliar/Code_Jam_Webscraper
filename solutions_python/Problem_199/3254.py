

inData  = open('large.in','r')
outData = open('large.out','w')

lines = int(inData.readline())

for line in range(1,lines+1):
	res = 0
	data = inData.readline().split()
	s = data[0]
	sList = list(s)
	k = int(data[1])

	for i in range(len(sList)-k+1):
		if sList[i] == '-':
			res += 1
			for j in range(k):
				if sList[i+j] == '-':
					sList[i+j] = '+'
				else:
					sList[i+j] = '-'

	if sList.count('-') > 0:
		outData.write('Case #%d: IMPOSSIBLE\n' % line)
	else:
		outData.write('Case #%d: %d\n' % (line, res))
inData.close()
outData.close()
