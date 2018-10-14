T = input()

for t in range(T):
    C, J = map(int, raw_input().split())

    ans = 0
    if (C == 0 and J == 1) or (C == 1 and J == 0):
        B, F = map(int, raw_input().split())
        ans = 2
    elif (C == 0 and J == 2) or (C == 2 and J == 0):
        B1, F1 = map(int, raw_input().split())
        B2, F2 = map(int, raw_input().split())
        if B1 > B2:
            B1, B2, F1, F2 = B2, B1, F2, F1
        if F2 - B1 <= 720:
            ans = 2
        elif F1 + 1440 - B2 <= 720:
            ans = 2
        else:
            ans = 4
    elif C == 1 and J == 1:
        B1, F1 = map(int, raw_input().split())
        B2, F2 = map(int, raw_input().split())
        ans = 2

    print 'Case #%d: %d' % (t + 1, ans)
