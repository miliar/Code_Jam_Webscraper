for tc in range(int(input())):
    input()
    P = list(map(int, input().split()))
    print('Case #{}: {}'.format(tc + 1, min(sum((p + x - 1) // x - 1 for p in P) + x for x in range(1, 1001))))

