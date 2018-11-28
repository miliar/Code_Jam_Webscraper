def inbounds(i, j):
    return i >= 0 and j >= 0 and i < R and j < C

T = int(input())
for t in range(1, T+1):
    R, C = [int(_) for _ in input().split(" ")]
    cake = []
    for r in range(R):
        cake.append([ch for ch in input()])
    
    for i in range(R):
        for j in range(C):
            if cake[i][j] == '?':
                continue
            r = i
            c = j+1
            while inbounds(r, c) and cake[r][c] == '?':
                cake[r][c] = cake[i][j]
                c += 1
            c = j-1
            while inbounds(r, c) and cake[r][c] == '?':
                cake[r][c] = cake[i][j]
                c -= 1
    for i in range(R):
        for j in range(C):
            if cake[i][j] == '?':
                continue
            r = i+1
            c = j
            while inbounds(r, c) and cake[r][c] == '?':
                cake[r][c] = cake[i][j]
                r += 1
            r = i-1
            while inbounds(r, c) and cake[r][c] == '?':
                cake[r][c] = cake[i][j]
                r -= 1
    print("Case #{}:".format(t))
    for i in range(R):
        for j in range(C):
            print(cake[i][j], end="")
        print()