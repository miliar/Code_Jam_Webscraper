def check(x, mn, mx):
	global pairs
	pcheck = []
	x = str(x)
	if len(x) == 1:
		pass
	if len(x) == 2:
		if x[0] != x[1]:
			first = x[::-1]
			if int(first) > int(x):
				pcheck.append(int(first)) 
	if len(x) == 3:
		second =  x[1:]+x[0]
		third = x[-1]+x[0:-1]
		if second != x and second[0] != '0' and int(second) > int(x):
			pcheck.append(int(second))
		if third != x and third[0] != '0' and int(third) > int(x):
			pcheck.append(int(third))
	for item in pcheck:
		if item >= mn and item <= mx:
			pairs += 1
						
def recycle(numbers):
	global pairs
	pairs = 0
	parameters = numbers.split()
	for x in range(int(parameters[0]), int(parameters[1])+1):
		check(x,int(parameters[0]),int(parameters[1]))
	testcases.append(pairs)

testcases = []
pairs = 0

f = file('C-small-attempt2.in', 'r')

for line in f:
	if len(line.split()) > 1:
		recycle(line)
		
f.close()

f1 = file('outputC.txt', 'w')

for x in range(1, len(testcases)+1):
	f1.write("Case #"+str(x)+": "+str(testcases[x-1])+'\n')
	
f1.close()
