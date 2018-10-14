import bisect

if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        N, X = [int(s) for s in raw_input().split()]
        nums = [int(s) for s in raw_input().split()]
        nums.sort()

        total = 0
        while nums:
            a = nums.pop()
            b = X - a
            idx = bisect.bisect_right(nums, b)
            if idx:
                nums.pop(idx - 1)
            total += 1

        print 'Case #%d: %d' % (caseno + 1, total)
