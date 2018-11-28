import sys
f=open(sys.argv[1])
T = int(f.readline())
def gcd(x, y):
	if x<y:
		x, y=y, x
	if y == 0:
		return x
	else:
		return gcd(y, x%y)
for t in range(T):
	nums = f.readline().split()
	nums=map(int, nums)
	n = nums[0]
	nums = sorted(nums[1:])
	if n == 2:
		ans = nums[1] - nums[0];
	else:
		ans = gcd(nums[2]-nums[1], nums[1]-nums[0]);
		for i in range(3, n):
			ans = gcd(ans, nums[i] - nums[i-1]);
	if nums[1] % ans == 0:
		print "Case #" + str(t+1) + ": 0"
	else:
		print "Case #" + str(t+1) + ": " + str(ans - nums[1]%ans)
