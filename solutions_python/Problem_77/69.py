T = input()
for caseID in range(1,T+1):
    N = input()
    nums = map(int, raw_input().split())
    sortedNums = sorted(nums)
    cnt = 0
    for i in range(0,N):
        if nums[i] != sortedNums[i]:
            cnt+=1
    print "Case #%d: %d" % (caseID,cnt)
