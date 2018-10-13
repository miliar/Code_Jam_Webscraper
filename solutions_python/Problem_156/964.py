for t in range(int(input())):

    D = int(input())

    P = list(map(int, input().split()))
    ans = max(P)

    Z = 2
    while Z < ans:
        ans = min(ans, sum([(x - 1) // Z for x in P]) + Z)
        Z += 1

    print('Case #%d: %s' % (t + 1, ans))
