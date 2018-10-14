import fractions
f = open('B-large', 'r')
ut = open('largeut', 'w')



x = f.readline()

counter = 1
for line in f:
	
	list = line.split(' ')
	diff = []
	for i in range(1,len(list)):
		for j in range(i+1,len(list)):
			if(int(list[i]) - int(list[j]) != 0):
				diff.append(abs(int(list[i]) - int(list[j])))
	
	start = diff[0]
	
	for i in range(0,len(diff)):
		start = fractions.gcd(start, diff[i])

	svar = (start - int(list[1])%start)

	if(start == 1):
		svar = 0

	if(int(list[1])%start == 0):
		svar = 0

	s = str('Case #%d: ' % counter)
	ut.write(s)
	t = str(svar)
	t += '\n'
	ut.write(t)
	counter = counter+1






