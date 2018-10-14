#!/bin/python

T = int(raw_input().strip())


def split(n):
    left = n / 2
    right = n / 2 - 1 if n > 0 and n % 2 == 0 else n / 2
    return left, right


# even -> even and odd, odd -> even and even (45 -> 22,22) or odd and odd (91-> 45,45)
def getNextPair(n):
    # 91 -> 45,45 -> 22,22 22,22
    # 90 -> 45,44 -> 22,22 22,21 -> 11,10 10,10
    return [n[0] / 2, n[1] * 2 + n[2], n[2]] if n[0] % 2 == 1 else [n[0] / 2, n[1], n[1] + n[2] * 2]


def check_ans(nums, k):
    if k <= nums[1]:
        return split(nums[0])
    if k - nums[1] <= nums[2]:
        return split(nums[0] - 1)
    return None


for c in range(1, T + 1):
    N, K = map(int, raw_input().split())

    nums = [N, 1, 0]
    ans = None
    k = K
    while not ans:
        ans = check_ans(nums, k)
        if not ans:
            k -= nums[1] + nums[2]  # order doesn't matter as long as it's sorted
        nums = getNextPair(nums)
        # print nums

    print 'Case #' + str(c) + ': ' + ' '.join(map(str, ans))#, N, K
