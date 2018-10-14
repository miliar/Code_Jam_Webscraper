#!/usr/bin/python


def solve(S, p, ts):
    ans = 0
    for t in ts:
        if t >= 3 * p - 2:
            ans += 1
        elif S > 0 and t >= 3 * p - 4 and 3 * p - 4 >= 0:
            ans += 1
            S -= 1
    return ans

T = int(raw_input())
for i in range(T):
    nums = map(int, raw_input().split())
    print "Case #{}: {}".format(i + 1, solve(nums[1], nums[2], nums[3:]))

