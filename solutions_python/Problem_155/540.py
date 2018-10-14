T = int(input())

for t in range(1, T + 1):
    N, S = [x.strip() for x in input().split()]
    N = int(N)

    have = 0
    need = 0
    for i in range(N + 1):
        x = int(S[i])
        if x == 0:
            continue
        if have >= i:
            have += x
        else:
            need += i - have
            have = i + x
    print("Case #%d: %d" % (t, need))

