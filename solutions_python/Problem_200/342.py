from __future__ import division, print_function
import sys

def InputIterator():
    for line in sys.stdin:
        for value in line.split(): yield value

inp = InputIterator()

T = int(next(inp))
for t in range(T):
    N = [int(d) for d in next(inp)]

    sys.stdout.write('Case #{}: '.format(t+1))

    answer = 0
    for k in range(len(N), -1, -1):
        cur = N[:k]

        if k < len(N):
            if N[k] > 0:
                cur.append(N[k]-1)
            else:
                continue

        for i in range(k+1, len(N)):
            cur.append(9)

        for i in range(1, len(N)):
            if cur[i] < cur[i-1]:
                break
        else:
            print(int(''.join(str(d) for d in cur)))
            break
