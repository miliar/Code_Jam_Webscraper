def solve(N, P, G):
    ans = 0

    M = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
    }
    for g in G:
        M[g % P] += 1
    # print(G)
    # print(M)

    if P == 2:
        ans += M[0]

        ans += M[1] // 2
        ans += M[1] % 2
    elif P == 3:
        ans += M[0]

        new_ans = min(M[1], M[2])
        M[1] -= new_ans
        M[2] -= new_ans
        ans += new_ans

        ans += M[1] // 3
        M[1] %= 3

        ans += M[2] // 3
        M[2] %= 3

        if M[1] + M[2] > 0:
            ans += 1
    elif P == 4:
        ans += M[0]
        # print(ans)

        new_ans = min(M[1], M[3])
        M[1] -= new_ans
        M[3] -= new_ans
        ans += new_ans
        # print(ans)

        ans += M[1] // 4
        M[1] %= 4
        M[2] += M[1] // 2
        M[1] %= 2
        # print(ans)

        ans += M[3] // 4
        M[3] %= 4
        M[2] += M[3] // 2
        M[3] %= 2
        # print(ans)

        ans += M[2] // 2
        M[2] %= 2
        # print(ans)

        # print(M)
        if M[1] + M[2] + M[3] > 0:
            ans += 1
        # print(ans)

    return ans


T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split(' '))
    G = list(map(int, input().split(' ')))

    ANS = solve(N, P, G)
    print('Case #{}: {}'.format(t, ANS))
