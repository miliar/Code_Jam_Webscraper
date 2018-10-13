from sys import argv
cases = [line.strip().split(' ') for line in open(argv[1])][1:]
for c in xrange(len(cases)):
    case = cases[c]
    nums = [int(case[1][i]) for i in xrange(len(case[1]))]
    invite = 0
    standing = nums[0]
    for i in xrange(1,len(nums)):
        add = 0
        if nums[i] != 0 and standing < i:
            add = (i - standing)
        invite += add
        standing += nums[i] + add
    print 'Case #' + str(c+1) + ': ' + str(invite)