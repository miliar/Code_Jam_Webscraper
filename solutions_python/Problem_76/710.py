import itertools

#  google codejam  2011  problem  C
#  only works for small sized inputs
#  the large set would require solve a 1000 linear equations mod 2
#   NO TIME!

# U is a "universal" set  (candies in this case)
# S is a subset (an int, taken as a bitstring)

def xorsum(U,S):
	xor = 0
	for bit in range(len(U)):
		if (1<<bit) & S: 
			xor = xor ^ U[bit]
	return xor

T = int(raw_input())

case = 1
while case <= T:
	N = int(raw_input())
	line = raw_input()
	pieces = line.split()
	candies = [int(x) for x in pieces]
	
	# loop through subsets whose xorsum equals its complement's
	# find the maximal
	
	maximal = -1
	for subset in range(2**N):
		complement = ~subset & (2**N-1)
		if subset == 0 or complement == 0: continue   # non-empty
		if (xorsum(candies,subset) == xorsum(candies,complement)):
			value = 0
			for bit in range(N):
				if (1<<bit) & subset: value += candies[bit]
			
			maximal = max(maximal, value)
	
	print "Case #%d: %s" % (case, str(maximal) if maximal != -1 else "NO")
	case += 1
