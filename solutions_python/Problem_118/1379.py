import math
T = int(raw_input())

for i in range(T):
	count = 0
	line = raw_input().split(' ')
	x = int(line[0])
	y = int(line[1])
	j = math.trunc(math.sqrt(x))
	if j * j < x:
		j += 1
	while j * j <= y:
		if str(j) == str(j)[::-1]:
			temp = j * j
			if temp <= y and str(temp) == str(temp)[::-1]:
				count += 1
		j += 1
	print "Case #" + str(i + 1) + ": " + str(count)
	
