t = int(input())
for q in range(t):
    ac, aj = map(int, input().split())
    C = []
    for i in range(ac):
        C.append(list(map(int, input().split())))
    J = []
    for i in range(aj):
        J.append(list(map(int, input().split())))

    if ac <= 1 and aj <= 1:
        r = 2
    else:
        T = J if ac == 0 else C
        T.sort()

        if T[1][1] - T[0][0] <= 720:
            r = 2
        elif T[1][0] - T[0][1] >= 720:
            r = 2
        else:
            r = 4

    print("Case #{}: {}".format(q+1, r))
