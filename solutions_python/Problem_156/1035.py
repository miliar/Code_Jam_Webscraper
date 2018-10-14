#!/usr/bin/env python
# -*- coding:utf-8 -*-

from heapq import heappush, heappop
import copy

dic = {}
def f(heap):
    heap_key = copy.copy(heap)
    if dic.has_key(str(heap_key)):
        return dic[str(heap_key)]
    if heap[0] == (-1, 1):
        return 1
    tmp = heap[0]
    heappop(heap)
    tmp2 = tmp[0] / 2
    tmp3 = tmp[0] / 3

    heap2 = copy.copy(heap)
    heappush(heap, (tmp2, -tmp2))
    heappush(heap, (tmp[0] - tmp2, abs(tmp[0] - tmp2)))

    heappush(heap2, (tmp3, -tmp3))
    heappush(heap2, (tmp[0] - tmp3, abs(tmp[0] - tmp3)))

    # if heap == [(-3, 3), (-3, 3), (-3, 3)] or heap2 == [(-3, 3), (-3, 3), (-3, 3)]:
    #     print cnt, min( 1 + f(copy.copy(heap), cnt+1), 1 + f(copy.copy(heap2), cnt+1), (cnt + 1 + abs(heap[0][0])))
    # print(1 + f(copy.copy(heap), cnt+1), 1 + f(copy.copy(heap2), cnt+1), (cnt + 1 + abs(heap[0][0])))
    dic[str(heap_key)] = min( 1 + f(copy.copy(heap)), 1 + f(copy.copy(heap2)), abs(heap_key[0][0]))
    # print dic[str(heap_key)]
    return dic[str(heap_key)]

def main():
    n = input()
    for _ in range(n):
        global dic
        dic = {}

        d = input()
        p = map(int, raw_input().split())
        ans = max(p)
        cnt = 0

        heap = []
        for i in p:
            heappush(heap, (-i, i))

        ans = f(copy.copy(heap))
        # print('p={}'.format(p))
        while heap[0] != (-1, 1):
            # print(heap[0])
            tmp = heap[0]
            heappop(heap)
            # print(tmp)
            tmp2 = tmp[0] / 2
            # print(tmp2, tmp[0])
            heappush(heap, (tmp2, -tmp2))
            heappush(heap, (tmp[0] - tmp2, abs(tmp[0] - tmp2)))
            cnt += 1
            ans = min(ans, cnt + abs(heap[0][0]))

        print("Case #{}: {}".format(_+1, ans))

if __name__ == "__main__":
    main()
