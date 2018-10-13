T = int(input())
for i in range(T):
    res = "Case #{0}:".format(i+1)
    R, C = input().split()
    R, C = int(R), int(C)

    M = []
    for r in range(R):
        M.append(list(input()))
        for c in range(C):
            if (M[r][c] != "?"):
                k = 1
                while (c-k >= 0) and (M[r][c-k] == "?"):
                    M[r][c-k] = M[r][c]
                    k += 1

                while (c+1 < C) and (M[r][c+1] == "?"):
                    M[r][c+1] = M[r][c]
                    c += 1
    
    for c in range(C):
        for r in range(R):
            if (M[r][c] != "?"):
                k = 1
                while (r-k >= 0) and (M[r-k][c] == "?"):
                    M[r-k][c] = M[r][c]
                    k += 1

                while (r+1 < R) and (M[r+1][c] == "?"):
                    M[r+1][c] = M[r][c]
                    r += 1    
    
    for r in range(R):
        res += "\n"
        for c in range(C):
            res += M[r][c]
        
    print(res)
        