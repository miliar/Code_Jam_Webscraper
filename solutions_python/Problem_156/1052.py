def solve(f):
    n = int(f.readline())
    p = map(int, f.readline().strip().split(' '))
    ans = 99999999999999999
    num = max(p)
    for sp_time in range(1, num + 1):
        cnt = 0
        for num in p:
            cnt += (num - 1) / sp_time
        ans = min(ans, cnt + sp_time)
    return ans

i = open('B-large.in', 'r')

T = int(i.readline())
for c in range(T):
    print "Case #%d: %d" % (c + 1, solve(i))
i.close()
