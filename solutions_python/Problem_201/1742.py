import sys
from queue import Queue

def sortfn(l, r):
    mid = l + (r - l) // 2 + (r - l) % 2 - 1

    min_lr = min(abs(mid - l + 1), abs(mid - r)) - 1
    max_lr = max(abs(mid - l + 1), abs(mid - r)) - 1
    return (-min_lr, -max_lr, mid)

nums = int(sys.stdin.readline())

for a in range(nums):
    ln = sys.stdin.readline().split(' ')
    n = int(ln[0])
    k = int(ln[1])

    Q = [(0, n)]

    counter = 0
    while len(Q) > 0:
        T = sorted(Q, key=lambda x: sortfn(x[0], x[1]))
        Q = []

        #print("round")

        for l, r in T:
            mid = l + (r - l) // 2 + (r - l) % 2 - 1

            #print((mid, min_lr, max_lr))

            counter += 1

            if counter >= k:
                min_lr = min(abs(mid - l + 1), abs(mid - r)) - 1
                max_lr = max(abs(mid - l + 1), abs(mid - r)) - 1
                print('Case #' + str(a + 1) + ": " + str(max_lr) + " " + str(min_lr))
                Q = []
                break

            if mid > l:
                Q.append((l, mid))
            if r > mid + 1:
                Q.append((mid + 1, r))