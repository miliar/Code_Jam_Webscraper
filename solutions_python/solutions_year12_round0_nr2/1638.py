T = input()

for t in range(T):
    nums = raw_input().split(' ')
    N, S, P = int(nums[0]), int(nums[1]), int(nums[2])
    ans = 0
    for i in range(N):
        M = int(nums[i+3])
        if M >= 3*P-2:
             ans += 1
             continue
        if S > 0 and M >= P and M >= 3*P-4:
             ans += 1
             S -= 1
    print 'Case #%s: %s' % (t+1, ans)