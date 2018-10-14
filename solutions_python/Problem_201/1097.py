#! /usr/bin/env python3

import sys
import heapq


def solve(n: int, k: int):

    rooms = [-n]
    last_room = n

    for i in range(k):

        room = -heapq.heappop(rooms)
        last_room = room

        if room > 2:
            heapq.heappush(rooms, -(room // 2))
            heapq.heappush(rooms, -((room - 1) // 2))

        elif room > 1:
            heapq.heappush(rooms, -1)

    return last_room // 2, (last_room - 1) // 2


def main():
    f = open(sys.argv[1], 'r')

    for i, line in enumerate(f):

        if i == 0:
            continue

        parts = line.split(' ')
        res = solve(n=int(parts[0]), k=int(parts[1]))
        print('Case #{}: {} {}'.format(i, *res))
        # print('Case {}: {} {}'.format(line.strip(), *res))

if __name__ == '__main__':
    main()
