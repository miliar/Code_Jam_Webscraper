import fileinput
import math


inp = fileinput.input()

T = int(inp.readline())

for t in range(1,T+1):
    n = 0
    N,X = (int(a) for a in inp.readline().split())

    parts = sorted([int(x) for x in inp.readline().split()])

    n = 0

    while len(parts) >= 2:
        if parts[0] + parts[-1] <= X:
            parts = parts[1:-1]
        else:
            parts = parts[:-1]
        n += 1
            
    n += len(parts)

    print("Case #{}: {}".format(t, n))


