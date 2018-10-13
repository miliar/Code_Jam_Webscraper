#!/usr/bin/python
inf = open('in', 'r')
outf = open('out', 'w')

strs = inf.read().split("\n")

i = 0
while i < int(strs[0]):
    nums = strs[i+1].split(' ')
    answ = 0
    s = int(nums[1])
    p = int(nums[2])
    for score in nums[3:]:
        score = int(score)
        if (score+2)/3 >= p:
            answ += 1
        elif p > score:
            continue
        elif (score+4)/3 >= p and s > 0:
            answ += 1
            s -= 1
    print "Case #%d: %d" % (i + 1, answ)
    i += 1

inf.close()
outf.close()
