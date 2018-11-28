import sys

def gcd(a, b):
	if a < b:
		return gcd(b, a)
	if b == 0:
		return a
	if a % b == 0:
		return b
	return gcd(b, a%b)

def main():
	ncas = int(raw_input())
	for cas in range(1, ncas+1):
		nums = map(int, raw_input().split())
		size = nums[0]
		nums = nums[1:]
		t = 0;
		for n1 in nums:
			for n2 in nums:
				t = gcd(t, abs(n1-n2))
		if (nums[0] % t) == 0:
			print "Case #%d: %d" % (cas, 0) 
		else:
			print "Case #%d: %d" % (cas, t - (nums[0] % t) )

main()
