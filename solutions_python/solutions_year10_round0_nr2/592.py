from fractions import gcd

def fairwarning(inputfile,outputfile):
	input = open(inputfile,"rt")
	output = open(outputfile,"wt")
	ncases = int(input.readline())
	for nc in range(1,ncases + 1):
		nums = [int(x) for x in input.readline().split()[1:]]
		d = [x - nums[0] for x in nums[1:]]
		common = abs(reduce(gcd,d))
		t = (common - (nums[0] % common)) % common
		output.write("Case #%d: %d\n"%(nc,t))
		
		