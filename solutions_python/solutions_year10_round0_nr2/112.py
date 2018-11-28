import sys
import fractions

def gcd(numbers):
    return reduce(lambda x, y: fractions.gcd(x,y), numbers, 0)
    
C = input()

for c in xrange(C):
    nums = [int(n) for n in raw_input().strip().split(" ")]
    diffs = [abs(nums[i + 1] - nums[1]) for i in range(1, nums[0])]
    T = gcd(diffs)
    wait = [-nums[i + 1] % T for i in xrange(nums[0])]
    print "Case #"+str(c+1)+":", max(wait)
