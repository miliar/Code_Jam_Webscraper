T = input()
for t in range(T):
    val = 0

    num = 0
    smax, nums = raw_input().split()
    smax = int(smax)

    for s in range(smax+1):
        d = s-num if s>num else 0
        val += d
        num += d + int(nums[s])

    print "Case #%d: %d"%(t+1, val)


