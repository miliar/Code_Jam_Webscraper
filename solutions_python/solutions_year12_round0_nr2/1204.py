import sys

f = open(sys.argv[1], "r")

f.readline()
line = f.readline()
tc = 1
while (line):
	count = 0
	nums = line.split()
	surprises = int(nums[1])
	p = int(nums[2])
	
	for i in range(3, len(nums)): # for each contestant
		score = int(nums[i])
		x = score / 3 # the minimum score with no surprises
		remainder = score % 3
		if (remainder == 0):
			if (x >= p):
				count += 1
			elif (surprises > 0 and x+1 >= p and x-1 >= 0):
				count += 1
				surprises -= 1
		elif (remainder == 1):
			if (x+1 >= p):
				count += 1
		else:
			if (x+1 >= p):
				count += 1
			elif (surprises > 0 and x+2 >= p):
				count += 1
				surprises -= 1
	print("Case #" + str(tc) + ": " + str(count))
	
	tc += 1
	line = f.readline()
	
f.close()
