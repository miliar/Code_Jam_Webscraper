#!/usr/bin/env python
MAX = 1000000
def fill_array(max_p):
    result = []
    for i in range(max_p + 1):
        result.append([MAX] * max_p)
    for i in range(max_p + 1):
        result[i][0] = i
        for j in range(1, i):
            min_t = MAX
            for k in range(1, i):
                now_t = MAX
                # first  = MAX
                # second = MAX
                for a in range(min(j, k)):
                    for b in range(min(j - a, i - k)):
                        temp_t = max(result[k][a], result[i - k][b])
                        if now_t > temp_t:
                            now_t = temp_t
                # for l in range(j):
                #     if result[i - k][l] < first:
                #         first = result[i - k][l]
                #     if result[k][l] < second:
                #         second = result[k][l]
                # now_t = max(first, second) # + 1
                if min_t > now_t:
                    min_t = now_t
            result[i][j] = min_t
    return result

def search_time(arr, P, i, time_add, max_p):
    if i >= len(P):
        return 0
    min_time = MAX
    for time in range(min(time_add + 1, P[i])):
        now_time = arr[P[i]][time]
        if now_time > max_p:
            continue
        next_time = search_time(arr, P, i + 1, time_add - time, max_p)
        now_time = max(now_time, next_time)
        if min_time > now_time:
            min_time = now_time
    return min_time

def solve(P, max_p):
    min_time = max_p
    time = fill_array(max_p)
    for time_add in range(max_p):
        time_now = search_time(time, P, 0, time_add, max_p)
        time_now += time_add
        if time_now < min_time:
            min_time = time_now
    return min_time

T = input()
for t in range(T):
    D = input()
    P = map(int, raw_input().split())[:D]
    print 'Case #%d: %s' % (t + 1, solve(P, max(P)))
