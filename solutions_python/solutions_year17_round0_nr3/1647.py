import math
# from collections import deque
import heapq
from collections import defaultdict

# def reduce_stalls(l):
#     max_ind, max_val = max(enumerate(l), key=lambda x: x[1])
#     left = math.floor((max_val - 1) / 2)
#     right = math.ceil((max_val - 1) / 2)
#     return l[:max_ind] + [left, right] + l[max_ind+1:], left, right

if __name__ == "__main__":
    cases = int(raw_input())
    for case in range(1, cases+1):
        n, k = map(int, raw_input().split(' '))
        if n == k:
            print("Case #{}: 0 0".format(case))
            continue
        # l = [n]
        # q = deque()
        q = []
        cts = defaultdict(int)
        cts[n] = 1
        max_val = n
        while k > 0:
            count = cts[max_val]
            if count == 0:
                max_val = -(heapq.heappop(q))
                continue
            cts[max_val] = 0
            left = (max_val - 1) // 2
            if (max_val - 1) % 2 == 0:
                right = left
                heapq.heappush(q, -right)
                cts[right] += 2 * count
            else:
                right = left + 1
                heapq.heappush(q, -right)
                cts[right] += count
                heapq.heappush(q, -left)
                cts[left] += count
            # print(q, cts)
            # raw_input()
            k -= count
            max_val = -(heapq.heappop(q))
        # for i in range(k):
        #     l, left, right = reduce_stalls(l)
        print("Case #{}: {} {}".format(case, right, left))
