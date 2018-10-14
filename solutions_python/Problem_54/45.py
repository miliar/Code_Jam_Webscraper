from fractions import gcd

#f = open("B-small-attempt0.in")
import sys
f = sys.stdin

t = int(f.readline().strip())

for i in range(t):
    nums = [int(x) for x in f.readline().strip().split()]
    n = nums[0]
    g = abs(nums[2] - nums[1])
    for j in range(2, n+1):
        g = gcd(g, abs(nums[j] - nums[j-1]))
    print "Case #%d: %d" % (i+1, (g-nums[1]%g)%g)

