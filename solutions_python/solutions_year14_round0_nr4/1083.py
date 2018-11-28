import sys

lines = sys.stdin.readlines()
T = int(lines[0])

def count(l1, l2, N):
    n2 = 0
    points = 0
    for n1 in range(N):
        while n2 < N and l1[n1] > l2[n2]:
            points += 1
            n2 += 1
        n2 += 1
    return points

for t in range(T):
    N = int(lines[t * 3 + 1])
    l1 = sorted(map(float, lines[t * 3 + 2].split()))
    l2 = sorted(map(float, lines[t * 3 + 3].split()))
    print('Case #{}: {} {}'.format(t + 1, N - count(l2, l1, N), count(l1, l2, N)))

