import sys

# sys.stdin = open('b.in', 'r')
sys.stdin = open('B-small-attempt3.in', 'r')
sys.stdout = open('B-small-attempt3.out', 'w')
# sys.stdin = open('A-large.in', 'r')
# sys.stdout = open('A-large.out', 'w')

eps = 1e-9

for t in range(int(input())):

    N, V, X = input().split()
    N = int(N)
    V = float(V)
    X = float(X)

    R, C = zip(*[map(float, input().split()) for n in range(N)])

    result = 0

    # print(R, C)

    if min(C) - eps > X or max(C) + eps < X:

        result = 'IMPOSSIBLE'

    else:

        if N == 1 or N == 2 and abs(C[0] - C[1]) < eps:
            result = '%.9f' % (V / sum(R))

        elif N == 2:
            v1 = V / (C[0] - C[1]) * (X - C[1])
            v2 = V - v1
            result = '%.9f' % max(v1 / R[0], v2 / R[1])

    print('Case #%d: %s' % (t + 1, result))

sys.stdin.close()
sys.stdout.close()