import sys

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
NbTests = int(input())  # read a line with a single integer
lsN = []    #cote d'un carre
lsM = []    #nb de modeles places
lsMP = []   #liste de liste de modeles places
for i in range(NbTests):
    n, m = str(sys.stdin.readline()).replace('\n', '').split()
    lsN.append(int(n))
    lsM.append(int(m))
    lsMP.append([])
    for j in range(int(m)):
        mod, r, c = str(sys.stdin.readline()).replace('\n', '').split()
        lsMP[i].append([mod, int(r), int(c)])

grid = []
Max = 0
listeFinale = []

def isGoodGrid():
    global grid
    global N
    #Bon pour les lignes et les colonnes
    for i in range(1, N + 1):
        cmptl = 0
        cmptc = 0
        for j in range(1, N + 1):
            if grid[i][j] == 'o' or grid[i][j] == 'x':
                cmptl+= 1
            if grid[j][i] == 'o' or grid[j][i] == 'x':
                cmptc+= 1
        if cmptl > 1 or cmptc > 1:
            print("Mauvaise colonne ou ligne")
            return False
    #bon pour diag r + c = k
    r = range(1, N + 1)
    for d in range(2, 2 * N):
        cmpt = 0
        for i in r:
            j = d - i
            if j >= 1 and j <= N:
                if grid[i][j] == 'o' or grid[i][j] == '+':
                    cmpt+= 1
        if cmpt > 1:
            return False

    for d in range(1 - N, N - 1):
        cmpt = 0
        for i in r:
            j = d + i
            if j >= 1 and j <= N:
                if grid[i][j] == 'o' or grid[i][j] == '+':
                    cmpt+= 1
        if cmpt > 1:
            return False
    return True

def diag1x(r, c):
    global N
    if (r + c) > N:
        return 0
    else:
        return r + c

def diag1y(r, c):
    global N
    if (r + c) > N:
        return (r + c) % (N + 1) + 1
    else:
        return 0

def diag2x(r, c):
    global N
    if (c - r) >= 0:
        return 0
    else:
        return r - c

def diag2y(r, c):
    global N
    if (c - r) > 0:
        return c - r
    elif (c - r) == 0:
        return N
    else:
        return 0



def afficherGrid():
    global grid
    print("")
    deb = 1
    for i in range(deb, len(grid)):
        temp = ""
        for j in range(deb, len(grid)):
            temp += str(grid[i][j]) + " "
        print(temp)

def addTile(tile):
    global N
    global grid
    r = tile[1]
    c = tile[2]
    m = tile[0]
    grid[r][c] = m
    if m != '+':
        grid[r][0] += 1
        grid[0][c] += 1
    if m != 'x':
        grid[diag1x(r,c)][diag1y(r,c)] += (N + 1)
        grid[diag2x(r,c)][diag2y(r,c)] += (N + 1) ** 2
    grid[0][0] += 1
    if m == 'o':
        grid[0][0] += 1

def removeTile(tile):
    global N
    global grid
    r = tile[1]
    c = tile[2]
    m = tile[0]
    grid[r][c] = '.'
    if m != '+':
        grid[r][0] -= 1
        grid[0][c] -= 1
    if m != 'x':
        grid[diag1x(r,c)][diag1y(r,c)] -= (N + 1)
        grid[diag2x(r,c)][diag2y(r,c)] -= (N + 1) ** 2
    grid[0][0] -= 1
    if m == 'o':
        grid[0][0] -= 1

def init(listeModeles):
    global grid
    global N
    global Max
    global listeFinale
    Max = 0
    listeFinale = []
    grid = []
    grid.append([0] * (N + 1))
    for i in range(1, N + 1):
        grid.append([0] + ['.'] * N)
    for tile in listeModeles:
        addTile(tile)
    #afficherGrid()

def isPossible(tile):
    global grid
    global N
    r = tile[1]
    c = tile[2]
    m = tile[0]
    if m != '+':
        if grid[r][0] % (N+1) != 0 or grid[0][c] % (N+1) != 0:
            return False
    if m != 'x':
        #print("diag1", diag1x(r,c), diag1y(r,c), grid[diag1x(r,c)][diag1y(r,c)])
        if (grid[diag1x(r,c)][diag1y(r,c)] // (N + 1)) % (N + 1)  != 0:
            return False
        #print("diag2", diag2x(r,c), diag2y(r,c), grid[diag2x(r,c)][diag2y(r,c)])
        if (grid[diag2x(r,c)][diag2y(r,c)] // (N + 1)**2) != 0:
            return False
    #print("isPossible", m, r, c)
    return True

def remplir(NN, listeModeles):
    global grid
    global M
    global N
    global listeFinale
    global Max
    N = NN
    init(listeModeles)
    #afficherGrid()
    listeAjouts = []
    Max = 0
    listeFinale = []
    nbO = 0
    if N == 1:
        Max = 2
        if grid[1][1] == 'o':
            return
        else:
            tile = ['o', 1, 1]
            addTile(tile)
            listeFinale.append(tile)
            return

    for i in range(1, N+1):
        if grid[1][i] == 'x':
            tile = ['x', 1, i]
            removeTile(tile)
            tile = ['o', 1, i]
            listeFinale.append(tile)
            addTile(tile)
            nbO = i
            break
        elif grid[1][i] == 'o':
            nbO = i
            break
    for i in range(1, N + 1):
        if grid[1][i] == '.':
            if nbO <= 0:
                tile = ['o', 1, i]
                nbO = i
            else:
                tile = ['+', 1, i]
            listeFinale.append(tile)
            addTile(tile)
    #afficherGrid()
    if nbO == 0:
        tile = ['+', 1, 1]
        removeTile(tile)
        tile = ['o', 1, 1]
        listeFinale.append(tile)
        addTile(tile)
        nbO = 1

    x = 2
    y = 1
    if(N == 1):
        return
    elif N == 2:
        if nbO == 1:
            tile = ['x', 2, 2]
        else:
            tile = ['x', 2, 1]
        listeFinale.append(tile)
        addTile(tile)
        Max = grid[0][0]
        #afficherGrid()
        return

    while(x < N):
        if y == nbO:
            y += 1
        tile = ['x', x, y]
        listeFinale.append(tile)
        addTile(tile)
        x += 1
        y += 1
    if nbO != N:
        for y in range(2, N):
            tile = ['+', N, y]
            listeFinale.append(tile)
            addTile(tile)
        tile = ['x', N, N]
        listeFinale.append(tile)
        addTile(tile)
    else:
        for y in range(2, N - 1):
            tile = ['+', x, y]
            listeFinale.append(tile)
            addTile(tile)
        tile = ['o', x, N - 1]
        listeFinale.append(tile)
        addTile(tile)
    Max = grid[0][0]
    if Max != N + 2 * (N - 1):
        print("**************************")
        print(Max, N + 2 * (N - 1), N)
        if N < 10:
            afficherGrid()
    cmpt=0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if grid[i][j] == 'x' or grid[i][j] == '+':
                cmpt += 1
            elif grid[i][j] == 'o':
                cmpt += 2
    if Max != cmpt:
        print("**************************")
        print(Max, cmpt)
    if not isGoodGrid():
        print("YAAAAAAAAAAAAAAAAAAAAARRRRRRRRRRRRRRRRR")
    #afficherGrid()

for i in range(1, NbTests + 1):
    remplir(lsN[i - 1], lsMP[i - 1])
    print("Case #{}: {} {}".format(i, Max, len(listeFinale)))
    for l in listeFinale:
        print("{} {} {}".format(l[0], l[1], l[2]))
    #for ls in lsMP[i-1]:
    #    listeFinale.append(ls)
    #init(listeFinale)
    #afficherGrid()
