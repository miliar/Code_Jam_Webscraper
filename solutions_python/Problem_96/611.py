#!/usr/bin/python3



def calc_best_common(T):
	"""
	Return the Best values associated and if it is useful for a surprise
	"""
	# Normal T = 3*b + d
	[b,d] = divmod(T,3)
	return (b + min(d,1), d!=1)
	

def calc_n_over(Tlist, B, S):
	"""
	Return the number of elements with best equal or higher to B
	"""
	
	res = 0
	for T in Tlist:
		Bn, use = calc_best_common(T)
		if Bn>=B:
			res += 1
			continue
		
		# For too small T there is no option for the surprise
		if T<2:
			continue
		# Consider it as a surprise result
		if use and S>0 and Bn+1>=B:
			S -= 1
			res += 1
	return res
	

import sys		
# Now read the input and decode it
if len(sys.argv)<2:
	fd = sys.stdin
else:
	fd = open(sys.argv[1],"r")

T = int(fd.readline().strip())
	
for i in range(T):
	
	vals = [ int(x) for x in fd.readline().strip().split() ]
	
	N = vals[0]
	S = vals[1]
	p = vals[2]
	Tlist = vals[3:]
	assert(len(Tlist)==N)
	print("Case #%d: %d" % (i+1, calc_n_over(Tlist, p, S)))

fd.close()



	
	
	
