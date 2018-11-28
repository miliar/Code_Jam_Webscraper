#!/bin/env python
from collections import deque

def solvec(f, case):
    s = int(f.readline().split()[0])
    arr = deque(sorted(map(int, f.readline().split())))
    solve(s, arr, case)

def solve(s, arr, case):
    # print(s, arr)
    ops = 0
    while len(arr):
        if s > arr[0]:
            s += arr[0]
            arr.popleft()
        else:
            if len(arr) == 1:
                ops += 1
                break
            else:
                if s + s - 1 > arr[0]:
                    ops += 1
                    s += s - 1 + arr[0]
                    arr.popleft()
                else:
                    for i in range(2, len(arr)):
                        s2 = s
                        for j in range(i):
                            s2 += s2 - 1
                        count = 0
                        for j in range(len(arr)):
                            if s2 > arr[j]:
                                s2 += arr[j]
                                count += 1
                            else:
                                break
                        if count > i:
                            for k in range(count):
                                arr.popleft()
                            ops += i
                    else:
                        ops += len(arr)
                    break
    print('Case #%d: %d' % (case + 1, ops))




def solvea(file):
    with open(file, 'r') as f:
        n = int(f.readline())
        for i, c in enumerate(range(n)):
            solvec(f, i)

if __name__=='__main__':
    import sys
    solvea(sys.argv[1]);
