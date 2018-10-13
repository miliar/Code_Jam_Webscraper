def calculate(N, K):
    max_value = 0
    min_value = 0
    group = {}

    if N != K:
        while K > 0:
            count = 1
            if N in group:
                count = group[N]
                group[N] = 0
            K -= count
                
            if N % 2:
                left_N = N // 2
            else:
                left_N = N // 2 - 1
            right_N = N // 2

            if left_N not in group:
                group[left_N] = count
            else:
                group[left_N] += count

            if right_N not in group:
                group[right_N] = count
            else:
                group[right_N] += count

            if K < 1:
                max_value = right_N
                min_value = left_N
                break

            N = max(group.keys())
            while group[N] == 0:
                del group[N]
                N = max(group.keys())

    return (max_value, min_value)

T = int(input())
for i in range(1, T + 1):
    N, K = [int(s) for s in input().split(' ')]
    y, z = calculate(N, K)
    print('Case #{}: {} {}'.format(i, y, z))
