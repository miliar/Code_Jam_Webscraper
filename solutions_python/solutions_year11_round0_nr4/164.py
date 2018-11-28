T = input()
for t in range(T):
    N = input()
    line = raw_input()
    nums = [int(i) for i in line.split()]

    res = 0
    for i, num in enumerate(nums):
        if num - 1 != i:
            res += 1

    print 'Case #%d: %f' % (t+1, res)

