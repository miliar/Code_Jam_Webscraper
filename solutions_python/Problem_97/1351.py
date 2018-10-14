from sys import *

def solve(_, nums):
    if len(nums) != 2:
        print "Case #%d:" %(_+1), 0
    e = range(nums[0],nums[1] + 1)
    res = {}
    for i in e:
        one = str(i)
        if (i > 11) and (len(one) == len(str(nums[1]))):
            for j in range(1,len(one)):
                new =  one[-j:] + one[:len(one) - j]
                a = int(one)
                b = int(new)
                if (a != b) and (b >= nums[0]) and (b <= nums[1]) and (new + ' ' + one not in res) and (one + ' ' + new not in res):
                    res[one + ' ' + new] = 0

    print "Case #%d:" %(_+1),
    print len(res)
    
cases = int(raw_input())
for _ in xrange(cases):
    nums = map(int,stdin.readline().split())
    solve(_,nums)