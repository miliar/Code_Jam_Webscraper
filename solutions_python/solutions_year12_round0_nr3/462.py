#!/usr/bin/python

def solve(A, B):
    ans = 0
    for i in range(A, B + 1):
        n = str(i)
        values = dict()
        for j in range(len(n)):
            m = n[j:] + n[0:j]
            if int(m) > i and int(m) <= B and m not in values:
                ans += 1
                values[m] = True
    return ans

T = int(raw_input())
for i in range(T):
    nums = map(int, raw_input().split())
    print "Case #{}: {}".format(i + 1, solve(nums[0], nums[1]))
