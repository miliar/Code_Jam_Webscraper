f = open('A-small-attempt3.in', 'rU')
o = open('out3.txt', 'w')
j = 0
k = 0
for line in f:
	k = k + 1
   	if len(line) > 2:
   		if (k > 1):
	   		j = j + 1
		   	friends = stoodup = 0
		   	i = 2
		   	audience = int(line[0])
		   	while (i <= audience + 2):
		   		if (i == 2 and int(line[i]) == 0):
		   			friends = friends +1
		   			stoodup = stoodup + 1
		   		elif (int(line[i]) != 0 and i !=2):
		   			if (stoodup<i-2):
		   				friends = friends + (i-2 - stoodup)
		   				stoodup = stoodup + (i-2 - stoodup)
		   		stoodup = stoodup + int(line[i])
		   		i = i+1		   		
		   	print >> o, "Case #" + str(j) + ": " + str(friends)


