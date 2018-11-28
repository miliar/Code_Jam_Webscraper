from sys import stdin

def solve(t):
    line = stdin.readline().split(' ')
    n = int(line[0])
    k = int(line[1])

    v1 = n # bigger
    cnt1 = 1
    cnt2 = 0
    base = 0

    while base + cnt1 + cnt2 < k:
        base += cnt1 + cnt2
        if v1 % 2 == 0:
            v1_ = v1 // 2
            # v2_ = v1 // 2 - 1
            cnt1_ = cnt1
            cnt2_ = cnt1 + 2 * cnt2
        else:
            v1_ = (v1 - 1) // 2
            # v2_ = (v1 - 1) // 2
            cnt1_ = 2 * cnt1 + cnt2
            cnt2_ = cnt2

        v1 = v1_
        cnt1 = cnt1_
        cnt2 = cnt2_

    if k <= base + cnt1:
        s = v1
    else:
        s = v1 - 1

    # print(s, v1, cnt1, cnt2)

    if s % 2 == 0:
        res1 = s // 2
        res2 = s // 2 - 1
    else:
        res1 = res2 = (s - 1) // 2

    print('Case #' + str(t + 1) + ': ' + str(res1) + ' ' + str(res2))

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
