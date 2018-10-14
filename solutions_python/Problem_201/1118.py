from sortedcontainers import SortedList, SortedDict
from math import floor, ceil


def solve(n, k):
    spaces = SortedDict()
    spaces[n] = 1
    ans_l, ans_r = -1, -1

    i = 0
    while i < k:
        # print(spaces)
        largest_space, n_largest_space = spaces.popitem()

        ans_l = floor((largest_space - 1) / 2)
        ans_r = ceil((largest_space - 1) / 2)

        if ans_l not in spaces:
            spaces[ans_l] = 0
        spaces[ans_l] += n_largest_space

        if ans_r not in spaces:
            spaces[ans_r] = 0
        spaces[ans_r] += n_largest_space
        i += n_largest_space

    return max(ans_l, ans_r), min(ans_l, ans_r)


def solve_bruteforce(n, k):
    spaces = SortedList()
    spaces.add(n)
    ans_l, ans_r = -1, -1

    for i in range(k):
        largest_space = spaces.pop()
        ans_l = floor((largest_space - 1) / 2)
        ans_r = ceil((largest_space - 1) / 2)
        spaces.add(ans_l)
        spaces.add(ans_r)

    return max(ans_l, ans_r), min(ans_l, ans_r)


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split(" "))

    ANS_max, ANS_min = solve(N, K)
    print("Case #{}: {} {}".format(t, ANS_max, ANS_min))
