
from collections import namedtuple
from queue import Queue
import heapq
from math import floor, ceil
import random

def calc_last_LR_space(N, K):
    bfs_queue = []
    heapq.heappush(bfs_queue, -N)
    left = right = 0
    for i in range(K):
        longest_stalls = -heapq.heappop(bfs_queue)
        left = floor((longest_stalls - 1)/2)
        right = longest_stalls -1 - left
        if right > 0:
            heapq.heappush(bfs_queue, -right)
        if left > 0:
            heapq.heappush(bfs_queue, -left)
        #print(i, longest_stalls, left, right, bfs_queue)
    return right, left



def calc_last_LR_space2(N, K):

    right = ceil((N - 1) / 2)
    left = N - 1 - right
    if K == 1:
        return right, left
    k_right = ceil((K-1)/2)
    k_left = K - 1 - k_right
    if k_right > k_left:
        return calc_last_LR_space2(right, k_right)
    else:
        return calc_last_LR_space2(left, k_left)

if __name__ == '__main__':
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        N, K = map(int, input().split())
        max_LR, min_LR = calc_last_LR_space2(N, K)
        print("Case #{}: {} {}".format(i, max_LR, min_LR))

    for i in range(1, 1000):
        k = random.randint(1, i)
        if not calc_last_LR_space2(i, k) == calc_last_LR_space(i, k):
            print (i, k, calc_last_LR_space2(i, k), calc_last_LR_space(i, k))