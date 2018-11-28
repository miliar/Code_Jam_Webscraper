import math
f= open("data")
T = int(f.readline().strip("\n"))
case = 0
while T > 0:
	case += 1
	T -= 1
	line = f.readline().strip("\n")
	cakes, num = line.split(' ')
	num = int(num)
	cakes = [c for c in cakes]
	count = 0
	for i in range(len(cakes)-num+1):
		if cakes[i]!='+':
			count += 1
			for k in range(i,i+num):
				if cakes[k] == '+':
					cakes[k] = '-'
				else:
					cakes[k] = '+'
	flag = 1
	for i in range(len(cakes)):
		if cakes[i] == '-':
			flag = 0
	if flag == 1:
		print "Case #"+str(case)+":",int(count)
	else:
		print "Case #"+str(case)+":",'IMPOSSIBLE'
