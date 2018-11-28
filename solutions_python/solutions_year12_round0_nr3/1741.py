import os, sys

infile = open(sys.argv[1], "r")
T = int(infile.readline())

for x in xrange(1, T+1):
    A, B = map(int, infile.readline().split())
    nums = range(B, A-1, -1)
    pairs = {}
    total = 0
    for y in xrange(len(nums)):
        check = str(nums[y])
        count = 0
        while count < len(check):
            check = check[-1] + check[:-1]
            if A <= int(check) < nums[y]:
                if not (int(check), nums[y]) in pairs:
                    total += 1
                    pairs[(int(check), nums[y])] = 1
            count += 1
    print "Case #%d: %d" % (x, total)