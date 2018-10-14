infile = open('file.in','r')
outfile = open('out.txt','w')
t = int(infile.readline())
for i in range(t):
	n = int(infile.readline())
	nums = infile.readline().split()
	prevNum =0
	totalDrop = 0
	maxDrop = 0
	case2 = 0
	for j in nums:
		num = int(j)
		drop = prevNum-num
		if drop > 0:
			totalDrop+=drop
			if drop > maxDrop:
				maxDrop = drop
		prevNum = num
	for j in range(len(nums[:-1])):
		num = int(nums[j])
		if num >= maxDrop:
			case2 +=maxDrop
		else:
			case2 +=num
	outfile.write("Case #"+str(i+1)+": " +str(totalDrop)+ " " + str(case2)+"\n")
