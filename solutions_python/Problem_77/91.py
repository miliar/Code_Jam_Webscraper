

def read_ints():
    return map(int, raw_input().split(" "))

T, = read_ints()
for cas in range(T):
    N, = read_ints()
    
    nums = [i-1 for i in read_ints()]
    marks = [-1] * N

    ans = 0
    for n in nums:
        if marks[n] == -1:
            tmp = n
            cnt = 0
            while marks[tmp] == -1:
                cnt += 1
                marks[tmp] = 0
                tmp = nums[tmp]
            if cnt > 1:
                ans += cnt
    print "Case #%d: %.6f" % (cas+1, ans)

