from __future__ import division, print_function
import sys

def InputIterator():
    for line in sys.stdin:
        for value in line.split(): yield value

inp = InputIterator()

T = int(next(inp))
for t in range(T):
    N, K = int(next(inp)), int(next(inp))

    N1, N2 = N+1, N
    Q1, Q2 = 0, 1

    sys.stdout.write('Case #{}: '.format(t+1))
    while K > 0:
        if Q1 >= K:
            print(N1//2, (N1-1)//2)
            break

        K -= Q1

        if Q2 >= K:
            print(N2//2, (N2-1)//2)
            break

        K -= Q2

        N1t, N2t = N1//2, (N2-1)//2
        Q1t, Q2t = 0, 0

        Q1t += Q1
        if (N1-1)//2 == N1t:
            Q1t += Q1
        else:
            Q2t += Q1

        Q2t += Q2
        if N2//2 == N1t:
            Q1t += Q2
        else:
            Q2t += Q2

        N1, N2, Q1, Q2 = N1t, N2t, Q1t, Q2t
