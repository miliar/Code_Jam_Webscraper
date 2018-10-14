import sys

def gcd(a,b):
	"""Return greatest common divisor using Euclid's Algorithm."""
	while b:
		a, b = b, a % b
	return a

def solve(orig_nums):
	nums = orig_nums[:]
	nums.sort()
	subs = []
	for i in range(len(nums)-1):
		subs.append(nums[i+1]-nums[i])
	#print "nums", nums
	#print "subs", subs
	T = reduce(gcd, subs)
	#print "T", T
	#print "%", nums[0] % T
	ans = ( (nums[0] / T + ((nums[0] % T)>0 and 1 or 0)) * T ) - nums[0]
	return ans


T = int(sys.stdin.readline())

for t in range(T):
	line = sys.stdin.readline().split()
	nums = map(int, line[1:])
	#print nums
	ans = solve(nums)
	print "Case #%d: %d" % (t+1, ans)



