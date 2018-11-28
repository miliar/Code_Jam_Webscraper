import fractions


def multi_gcm(nums):
	return reduce(fraction.gcm, nums)
	

def lcm(a,b):
	return a*b//fractions.gcd(a,b)
	

def multi_lcm(nums):
	return reduce(lcm, nums)
	
def answer():
	param = [int(n) for n in raw_input().split(" ")]
	
	M = [int(n) for n in raw_input().split(" ")]
	pattern = []
	all_lcm = multi_lcm(M)
	#print all_lcm
	for i in xrange(all_lcm):
		for j in enumerate(M):
			if i%j[1] == 0:
				# index, data
				pattern.append(j)
				
	#print pattern
				
	return pattern[(param[1]-1)%len(pattern)][0]+1
	

def main():
	for i in xrange(input()):
		print "Case #{}: {}".format(i+1, answer())
	

if __name__ == "__main__":
	main()
	