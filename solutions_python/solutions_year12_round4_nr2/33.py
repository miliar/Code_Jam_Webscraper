def solve(N, W, H, rad):
    rs = [(rad[i], i) for i in range(N)]
    rs.sort(reverse=True)
    solution = [0 for i in range(N)]
    x0, y0 = 0, 0
    x1 = rs[0][0]
    for i in range(N):
        r, j = rs[i]
        if y0 > 0 and y0 + r > H:
            x0 = x1
            x1 += 2 * r
            y0 = 0
        if x0 == 0:
            x = 0
        else:
            x = x0 + r
        if y0 == 0:
            y = 0
            y0 += r
        else:
            y = y0 + r
            y0 += 2 * r
        solution[j] = (x, y)
    for i in range(N):
        assert 0 <= x <= W and 0 <= y <= H
        for j in range(i + 1, N):
            xi, yi = solution[i]
            xj, yj = solution[j]
#            print(rs[i][0], xi, xj, rs[j][0], yi, yj, (xj - xi) ** 2 + (yj - yi) ** 2, (rs[i][0] + rs[j][0]) ** 2)
#            print(abs(xj - xi), abs(yj - yi), abs(rad[i] + rad[j]))
            assert abs(xj - xi) >= abs(rad[i] + rad[j]) or abs(yj - yi) >= abs(rad[i] + rad[j])
    return solution

T = int(input ())
for i in range(1, T + 1):
    N, W, H = map(int, input().split())
    r = list(map(int, input().split()))
    solution = solve(N, W, H, r)
    print("Case #%d: " % i, end="")
    for i in range(N):
        print(solution[i][0], solution[i][1], end=" ")
    print()


