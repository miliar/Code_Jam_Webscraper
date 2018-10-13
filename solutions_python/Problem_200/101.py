T = int(raw_input())  

def get(s, l):
    nums = [int(c) for c in s]
    
    part1, part2 = "", ""
    for i in xrange(l):
        part1 += str(nums[i])
        if i < l - 1 and nums[i] > nums[i + 1]:
            part1 = get(str(int(part1) - 1), i + 1)
            part2 = '9' * (l - i - 1)
            return part1 + part2
    return part1 + part2

for K in xrange (T):
    s = raw_input()
    l = len(s)

    print "Case #{}: {}".format(K+1, get(s, l).strip("0"))
    