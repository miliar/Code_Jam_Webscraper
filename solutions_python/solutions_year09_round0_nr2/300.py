import string

def solve(M, H, W):
    letters = string.ascii_letters
    S = list()
    
    for x in range(H):
        S.append([])
        for y in range(W):
            S[x].append("")
            
    targets = list()
    for x in range(H):
        targets.append([])
        for y in range(W):
            targets[x].append(target(M, H, W, x, y))

    solved = False
    while solved == False:
        solved = True
        for x in range(H):
            for y in range(W):
                tx, ty = targets[x][y]
                if S[x][y] != S[tx][ty]:
                    solved = False
                    S[x][y] = S[tx][ty]
                if S[x][y] == "" and x == tx and y == ty:
                    solved = False
                    S[x][y] = letters[-1]
                    letters = letters[:-1]

    # Replace with ordered letters
    D = {}
    for x in range(H):
        for y in range(W):
            if S[x][y] not in D:
                D[S[x][y]] = letters[0]
                letters = letters[1:]
            S[x][y] = D[S[x][y]]
    return S
                        

def target(M, H, W, x, y):
    neighbors = []
    if x > 0 and M[x-1][y] < M[x][y]:
        neighbors.append((M[x-1][y], 1, (x-1, y)))
    if y > 0 and M[x][y-1] < M[x][y]:
        neighbors.append((M[x][y-1], 2, (x, y-1)))
    if y < W-1 and M[x][y+1] < M[x][y]:
        neighbors.append((M[x][y+1], 3, (x, y+1)))
    if x < H-1 and M[x+1][y] < M[x][y]:
        neighbors.append((M[x+1][y], 4, (x+1, y)))
    if len(neighbors) == 0:
        return x, y
    neighbors.sort()
    return neighbors[0][-1]
    
f = open("B-large.in.txt", "r")
T = int(f.readline().strip())

output = open("watershed_output.txt", 'w')
output.write("")
output.close()
output = open("watershed_output.txt", 'a')

for x in range(T):
    D = f.readline().split()
    H = int(D[0].strip())
    W = int(D[1].strip())
    M = []
    for row in range(H):
        row = f.readline().split()
        for y in range(len(row)):
            row[y] = int(row[y].strip())
        M.append(row)
    print "Case #" + str(x+1) + ":"
    S = solve(M, H, W)
    for row in S:
        print " ".join(row)
