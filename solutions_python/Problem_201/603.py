import sys, os, re, collections, heapq

def print_result (case_num, result):
    print('Case #{}: {}'.format(case_num + 1, result))

def n_to_yz (N):
    assert N >= 1
    return (N-1)//2, N//2

def solve (N,K):
    gapsizes = [-N]
    gaps = {N:1}
    while K > 0:
        cur = -heapq.heappop(gapsizes)
        cur_cnt = gaps[cur]
        del gaps[cur]
        if K <= cur_cnt:
            return n_to_yz(cur)
        K -= cur_cnt
        sub_left, sub_right = n_to_yz(cur)
        try:
            gaps[sub_left] += cur_cnt
        except KeyError:
            gaps[sub_left] = cur_cnt
            heapq.heappush(gapsizes,-sub_left)
        try:
            gaps[sub_right] += cur_cnt
        except KeyError:
            gaps[sub_right] = cur_cnt
            heapq.heappush(gapsizes,-sub_right)
    assert False

for case_num in range(int(input())):
    N,K = map(int,input().split())
    y,z = solve(N,K)
    print_result(case_num,'{} {}'.format(z,y))
