import math

num_cases = int(input())

for c in range(num_cases):
    N, K = map(int, input().split())
    HR = []
    for i in range(N):
        Ri, Hi = map(int, input().split())
        HR.append((Hi, Ri))

    HR = sorted(HR, key=lambda t: -t[1])

    max_result = 0
    for i in range(N):
        max_result = max(
            max_result,
            (
                sum(2 * Ri * Hi for Ri, Hi
                    in sorted(HR[i+1:], key=lambda t: -(t[0] * t[1]))[:K-1]) +
                2 * HR[i][1] * HR[i][0] +
                HR[i][1] * HR[i][1]
            ) * math.pi
        )
    print('Case #{}: {}'.format(c + 1, max_result))
