# coding: utf8

import sys
import heapq


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        N, K = map(int, sys.stdin.readline().split())
        heap = []
        heapq.heappush(heap, (-N, 1))
        last_one = None
        while K:
            curr_item = heapq.heappop(heap)
            last_one = curr_item
            to_split = min(curr_item[1], K)
            new_space = curr_item[0] + 1
            if new_space % 2 == 0:
                new_items = [
                    (new_space // 2, to_split * 2),
                ]
            else:
                new_items = [
                    (new_space // 2, to_split),
                    (new_space // 2 + 1, to_split),
                ]
            if to_split < curr_item[1]:
                new_items.append((curr_item[0], curr_item[1] - to_split))
            for new_item in new_items:
                heapq.heappush(heap, new_item)
            K -= to_split
            # hot-fix
            tmp = {}
            for item in heap:
                tmp[item[0]] = tmp.get(item[0], 0) + item[1]
            heap = list(tmp.items())
            heapq.heapify(heap)
        space = -last_one[0] - 1
        print('Case #%s: %s %s' % (_T + 1, space // 2 + space % 2, space // 2))


if __name__ == '__main__':
    main()
