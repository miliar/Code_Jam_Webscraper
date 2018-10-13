num_count = input()

for casenum in range(1, num_count+1):
	data = raw_input().split()
	cakes = list(data[0])
	length = int(data[1])
	
	flips = 0
	
	for i in range(len(cakes) - length,-1,-1):
		if(cakes[length-1+i] == '-'):
			for ptr in range(i,i+length):
				if(cakes[ptr] == '+'):
					cakes[ptr] = '-'
					continue
				cakes[ptr] = '+'
			flips += 1

	
	for i in range(0,len(cakes)):
		if(cakes[i] == '-'):
			flips = -1
			break

	if(flips==-1):
		print("Case #{}: IMPOSSIBLE".format(casenum))
		continue
	print("Case #{}: {}".format(casenum,flips))


