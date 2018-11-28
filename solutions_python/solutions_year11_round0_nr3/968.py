import sys

f = open(sys.argv[1])

n = int(f.readline())



for cidx in xrange(n):
    l = int(f.readline())
    nums = [int(x) for x in f.readline().split()]

    def xor(a,b):
        return a^b

    cry = reduce(xor, nums)

    if cry:
        print 'Case #%i: NO'% (cidx+1)
    else:
        nums.sort()
        nums.reverse()
        smax = []
        ln = len(nums)
        for idx in xrange(1,ln):
            #s = sum( nums[0:idx])
            s  = reduce(xor, nums[0:idx])
            sx = reduce(xor, nums[idx:])
            if s == sx:
#                print nums[0:idx],s, nums[idx:], sx
                smax.append(sum(nums[0:idx]))

        print 'Case #%i: %i' % (cidx+1,max(smax))
            
