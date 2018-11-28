import os

t = int(input())
for ti in range(1, t + 1):
	line = input().split()
	a = int(line[0])
	b = int(line[1])
	k = int(line[2])

	count = 0
	for ai in range(0, a):
		for bi in range(0, b):
			num = ai & bi
			if num < k:
				count += 1

	print("Case #" + str(ti) + ": " + str(count))

	#print(str(a) + " " +str(b) +" "+ str(k))