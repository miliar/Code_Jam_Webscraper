#!/usr/bin/env python

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

import sys
from Queue import Queue

def main():
    T = int(sys.stdin.readline().strip())
    for test in range(T):
        H, W = [int(v) for v in sys.stdin.readline().strip().split()]
        m = [
            [int(v) for v in sys.stdin.readline().strip().split()]
            for i in range(H)
        ]
        con = dict(
            ((i, j), []) for i in range(H) for j in range(W)
        )
        for i in range(H):
            for j in range(W):
                min = 0x3f3f3f3f
                minp = -1, -1
                for k in range(4):
                    _i = i + dx[k]
                    _j = j + dy[k]
                    if _i < 0 or _i >= H or _j < 0 or _j >= W:
                        continue
                    if m[_i][_j] < min:
                        min = m[_i][_j]
                        minp = _i, _j

                if min >= m[i][j]:
                    continue
                con[i, j].append(minp)
                con[minp].append((i, j))

        comp = [
            [-1 for i in range(W)]
            for j in range(H)
        ]
        Q = Queue()
        count = 0
        print "Case #%d:" % (test + 1)
        for i in range(H):
            for j in range(W):
                if comp[i][j] == -1:
                    Q.put((i, j))
                    comp[i][j] = count
                    while not Q.empty():
                        x, y = Q.get()
                        for _x, _y in con[x, y]:
                            if comp[_x][_y] != -1:
                                continue
                            comp[_x][_y] = count
                            Q.put((_x, _y))
                    count += 1
                print chr(ord('a') + comp[i][j]),
            print

    return 0

if __name__ == "__main__":
    main()

