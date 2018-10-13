if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        N = int(raw_input())
        nums = [int(s) for s in raw_input().split()]

        if reduce(lambda x, y: x ^ y, nums, 0) == 0:
            res = str(sum(nums) - sorted(nums)[0])
        else:
            res = 'NO'

        print 'Case #%d: %s' % (caseno + 1, res)

