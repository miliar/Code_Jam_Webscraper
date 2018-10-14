#!/usr/bin/python

N = int(raw_input())


def solve(in_num):
    def _is_tidy(num):
        arr_num = list(str(num))
        for k in range(0, len(arr_num) - 1):
            if int(arr_num[k]) <= int(arr_num[k + 1]):
                continue
            else:
                return False
        return True

    for j in xrange(in_num, 0, -1):
        # print('tri', j)
        if _is_tidy(j):
            return j


for i in range(0, N):
    raw_num = int(raw_input())
    print("Case #{}: ".format(i + 1) + str(solve(raw_num)))
