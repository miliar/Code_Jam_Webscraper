T = int(input())
for t in range(1, T + 1):
    R, C = map(int, input().split(" "))
    cake = list()
    for r in range(R):
        cake.append(list(input()))

    # down
    for r in range(1, R):
        for c in range(C):
            if cake[r][c] == '?':
                cake[r][c] = cake[r - 1][c]

    # up
    for r in range(R - 2, -1, -1):
        for c in range(C):
            if cake[r][c] == '?':
                cake[r][c] = cake[r + 1][c]

    # right
    for c in range(1, C):
        for r in range(R):
            if cake[r][c] == '?':
                cake[r][c] = cake[r][c - 1]

    # left
    for c in range(C - 2, -1, -1):
        for r in range(R):
            if cake[r][c] == '?':
                cake[r][c] = cake[r][c + 1]

    print("Case #{}:".format(t))
    for r in cake:
        print("{}".format(''.join(r)))
