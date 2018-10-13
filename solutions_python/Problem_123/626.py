import sys

def solve(A, others):
    others = sorted(others)

    ops = 0

    for idx in range(len(others)):
        ops_now = 0
        while A <= others[idx]:
            A += A - 1
            ops += 1
            ops_now += 1

            if ops_now >= len(others) - idx:
                return ops

        A += others[idx]

    return ops

n = int(sys.stdin.readline())

results = []
for i in xrange(n):
    A, N = map(int, sys.stdin.readline().split(' '))
    others = map(int, sys.stdin.readline().split(' '))
    results.append('Case #' + str(i+1) + ': ' + str(solve(A, others)))

sys.stdout.write('\n'.join(results))
