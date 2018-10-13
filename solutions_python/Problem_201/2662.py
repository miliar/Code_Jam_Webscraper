import sys
import numpy as np

def solve(n, k):
    stalls = ['o'] + n*['.'] + ['o']
    max_l_r = 0
    min_l_r = 0
    for _ in range(k):
        l_s = {}
        r_s = {}
        for i in range(len(stalls)):
            if stalls[i] == '.':
                l_cnt = 0
                li = i-1
                while li >= 0 and stalls[li] == '.':
                    l_cnt += 1
                    li -= 1
                r_cnt = 0
                ri = i+1
                while ri < len(stalls) and stalls[ri] == '.':
                    r_cnt += 1
                    ri += 1
                l_s[i] = l_cnt
                r_s[i] = r_cnt
        max_min = 0
        for key in l_s.keys():
            mn = min(l_s[key], r_s[key])
            if mn > max_min:
                max_min = mn
        max_min_indices = []
        for key in l_s.keys():
            mn = min(l_s[key], r_s[key])
            if mn == max_min:
                max_min_indices.append(key)
        max_max = 0
        for key in max_min_indices:
            mx = max(l_s[key], r_s[key])
            if mx > max_max:
                max_max = mx
        max_max_indices = []
        for key in max_min_indices:
            mx = max(l_s[key], r_s[key])
            if mx == max_max:
                max_max_indices.append(key)

        new_stall_index = max_max_indices[0]
        stalls[new_stall_index] = 'o'
        max_l_r = max(l_s[new_stall_index], r_s[new_stall_index])
        min_l_r = min(l_s[new_stall_index], r_s[new_stall_index])

    return "{} {}".format(max_l_r, min_l_r)

num_cases = int(sys.stdin.readline())
for case in range(num_cases):
    n, k = [int(x) for x in sys.stdin.readline().split()]
    print("Case #{}: {}".format(case+1, solve(n, k)))