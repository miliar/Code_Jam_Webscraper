def run(smax,nums):
	pos_ptr = 0
	reach_ptr = 0

	extra = 0
	while reach_ptr < smax:
		count = nums[pos_ptr]
		reach_ptr += count
		if reach_ptr == pos_ptr:
			extra += 1
			reach_ptr += 1
		pos_ptr += 1
	return extra


f = file('A-large.in','r')

lines = f.readlines()
T = int(lines[0].strip())

for i in xrange(1,len(lines)):
	line = lines[i]
	splits = line.strip().split(' ')
	smax = int(splits[0])
	nums = [int(j) for j in splits[1]]
	out = run(smax,nums)
	print "Case #" + str(i) + ": " + str(out)