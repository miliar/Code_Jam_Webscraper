import sys

nums = int(sys.stdin.readline())


def find_min(matrix, start, end):
    if start == end:
        return '0'
    dist = {}
    for g in range(len(matrix) + 1):
        dist[g] = float("inf")

    dist[start] = 0
    Q = set(range(len(matrix) + 1))

    while len(Q) > 0:
        u = min(Q, key=dist.get)
        Q.remove(u)
        if u == end:
            continue
        for v in matrix[u]:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
    if dist[end] == float("inf"):
        return "IMPOSSIBLE"
    return str(dist[end])

for a in range(nums):
    ln = sys.stdin.readline().split(' ')
    p = ln[0]
    n = 0
    for s in range(len(p)):
        n |= (1 if p[s] == '+' else 0) << s
    k = int (ln[1])
    result = 0
    target = (2 ** len(p)) - 1

    matrix = []

    flipper = 0
    for i in range(k):
        flipper |= (1 << i)

    for i in range(target):
        inner = []
        for j in range(len(p) - k + 1):
            inner.append(i ^ (flipper << j))
        matrix.append(inner)

    print('Case #' + str(a + 1) + ": " + find_min(matrix, n, target))