
f_in = open('B-small-attempt0.in', 'r')
f_out = open('B-small-attempt0.out', 'w')
lines = f_in.readlines()

for i in range(len(lines)):
	if (i == 0):
		continue
	
	f_out.write('Case #'+str(i)+': ')
	
	line = lines[i].strip()
	nums = line.split()
	N = int(nums[0])
	S = int(nums[1])
	p = int(nums[2])
	scores = nums[3:]
	
	num_successful = 0
	for score in scores:
		score = int(score)
		baseline = score / 3
		remainder = score % 3
		if remainder > 0:
			baseline += 1
		if baseline >= p:
			num_successful += 1
		elif S > 0 and ((baseline+1) >= p) and score >= 2:
			num_successful += 1
			S -= 1
	
	f_out.write(str(num_successful)+'\n')