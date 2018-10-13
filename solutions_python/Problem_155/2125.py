import os, sys, itertools
lines = [line.strip() for line in open("%s" % sys.argv[1])][::-1][:-1]
case = 0
while lines:
    case += 1
    invited = 0
    nums = map(int,lines.pop().split(' ')[-1])
    standing = nums.pop(0)
    if not standing:
        standing,invited = 1,1
    for shy,num in enumerate(nums,start=1):
        if standing < shy:
            invite = shy - standing
            invited += invite
            num += invite
        standing += num
    print "Case #%s:" % case,
    print invited

