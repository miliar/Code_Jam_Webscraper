C = int(raw_input())

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def gcdnums(nums):
    g = nums[0]
    for i in xrange(1, len(nums)):
        g = gcd(g, nums[i])
    return g

for case in xrange(1, C+1):
    line = map(int, raw_input().split())
    N = line[0]
    nums = line[1:]
    nums.sort()

    diff = []
    for i in xrange(1, len(nums)):
        diff.append(nums[i]-nums[i-1])
    T = gcdnums(diff)
    print "Case #%d: %d" % (case, ((T - nums[i]%T)%T))

