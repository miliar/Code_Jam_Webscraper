cases = int(raw_input())

seen = {}

def rots(st, lbound, ubound):
    global seen
    orig = int(st)
    count = 0
    for i in xrange(len(st)):
        res = int(st[i:] + st[:i])
        if len(str(res)) == len(st) and res >= lbound and res <= ubound and res < orig and (res, st) not in seen:
            count += 1
            seen[(res, st)] = 1
    return count

for i in xrange(cases):
    seen = {}
    nums = map(int, raw_input().split())
    count = 0
    for j in xrange(nums[0], nums[1]+1):
        count += rots(str(j), nums[0], nums[1])
    print "Case #%d: %d" % (i+1, count)

