testcases = int(input())
for t in range(1,testcases+1):
	numberarray = []
	line = input().split()
	a = int(line[0])
	b = int(line[1])
	c = int(line[2])
	final = 0
	for i in range(0,a):
		for j in range(0,b):
			check = i & j
			if check < c:
				final += 1
	print("Case #{0}: {1}".format(t, final))
