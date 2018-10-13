from sys import stdin

cases = int(stdin.readline())

memos = {}

def doit(s, p):
    if (s, p) in memos:
        return memos[(s, p)]
    thing = ()
    if p == 1:
        if s%2 is 0:
            thing = (s/2, s/2 - 1)
        else:
            thing = (s/2, s/2)
        memos[(s, p)] = thing
    else:
        p -= 1
        if s%2 is 0:
            if p%2 is 1:
                thing = doit(s/2, p/2 + 1)
            else:
                thing = doit(s/2 - 1, p/2)
        else:
            if p%2 is 1:
                thing = doit(s/2, p/2 + 1)
            else:
                thing = doit(s/2, p/2)
        memos[(s, p+1)] = thing
    return thing
    
for i in range(cases):
    nums = stdin.readline().split()
    stalls = int(nums[0])
    peeps = int(nums[1])
    ans = doit(stalls, peeps)
    print "Case #"+str(i+1)+": "+str(ans[0])+" "+str(ans[1])
