from decimal import *
getcontext().prec = 30

inputfile = open('B-large.in', 'r')
outputfile = open('B-large.out', 'w')
t = int(inputfile.readline())
for i in range(t):
	line = inputfile.readline().split()
	c = Decimal(line[0])
	f = Decimal(line[1])
	x = Decimal(line[2])
	r = Decimal(2.0)
	m = x / r
	s = 0
	while 1:
		
		s = s + (c / r)
		r = r + f
		n = s + (x / r)
		#print(str(s) + ' ' + str(r) + ' ' + str(n))
		if n < m:
			m = n
		else:
			break
		
	outputfile.write("Case #" + str(i+1) + ": ")
	outputfile.write(str(round(m, 7)))
	outputfile.write('\n')
outputfile.close()
	
