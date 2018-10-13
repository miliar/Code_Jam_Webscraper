import sys

if len(sys.argv) > 1:
	filename = sys.argv[1]
	f = open(filename,'r')
	count = 0
	
	outF = open('dancingSmallout.txt','w+')
	
	for line in f.readlines():
		if count > 0:
			out = "Case #%d: " % count 
			nums = line.split()
			N = int(nums[0])
			S = int(nums[1])	
			p = int(nums[2])
			max = 0
			for ind in range(3,3+N):
				t = int(nums[ind])
				ts = t/3.0
				if t < p:
					continue
				if ts > p-1:
					max = max + 1
				elif ts >p-2 and S > 0:
					max = max + 1
					S = S - 1
			out = out + str(max) + "\n"
			print out
			outF.write(out)
			outF.flush()
			count = count + 1
		else:
		 	count = count + 1
	outF.close()