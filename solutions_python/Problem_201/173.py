T = int(input())
for tid in range(T):
    d = {}
    N, K = [int(x) for x in input().split(' ')]
    d[N] = 1

    remaining = K
    while remaining > 0:
        max_key = -1
        max_value = -1
        for key, value in d.items():
            if max_key < key:
                max_key = key
                max_value = value
        a = max_key -1
        if remaining > max_value:
            remaining -= max_value
            del d[max_key]
            if a//2 not in d:
                d[a//2] = 0
            if a % 2 == 0:
                d[a//2] += 2 * max_value
            else:
                if (a//2 + 1) not in d:
                    d[a//2 + 1] = 0
                d[a//2] += max_value
                d[a//2 + 1] += max_value
        else:
            if a % 2 == 0:
                print('Case #{}: {} {}'.format(tid + 1, a//2, a//2))
            else:
                print('Case #{}: {} {}'.format(tid + 1, a//2 + 1, a//2))
            remaining = 0
