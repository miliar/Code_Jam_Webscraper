import sys


rl = sys.stdin.readline



T = int(rl())

def solve(A, N, arr, t):
    if A == 1:
        print 'Case #{0}: {1}'.format(t, len(arr))
        return

    arr = sorted(arr)
    N = len(arr)
    best = N
    cur = 0
    for i in range(N):
        if A > arr[i]:
            A = A + arr[i]
        else:
            x = 0
            while (A <= arr[i]):
                A = 2 * A - 1
                x += 1

            best = min(cur + N - i, best);
            cur += x;
            A += arr[i]
    print 'Case #{0}: {1}'.format(t, min(best, cur))

for t in range(1, T + 1):
    # read input
    A, N = map(int, rl().split())
    arr = map(int, rl().split())
    solve(A, N, arr, t)



