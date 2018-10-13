# true if (r, c) is in grid of size n
def in_grid(r, c, n):
    if r >= 0 and c >= 0 and r < n and c < n:
        return True
    else:
        return False

# returns list of (row, col) pairs that are in the same diagonal as input. n is the size of grid
def find_diag(r, c, n):
    all_pairs = []
    i, j = r, c
    while True:
        i += 1
        j += 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    i, j = r, c
    while True:
        i -= 1
        j += 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    i, j = r, c
    while True:
        i += 1
        j -= 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    i, j = r, c
    while True:
        i -= 1
        j -= 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    return all_pairs

# returns list of (row, col) pairs that are in the same row/column as input. n is the size of grid
def find_rowcol(r, c, n):
    all_pairs = []
    i, j = r, c
    while True:
        i += 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    i, j = r, c
    while True:
        i -= 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    i, j = r, c
    while True:
        j += 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    i, j = r, c
    while True:
        j -= 1
        if in_grid(i, j, n):
            all_pairs.append((i, j))
        else:
            break
    return all_pairs

def find_max(grid): #input is a list of lists
    n = len(grid)
    pluses = [['.' for i in range(n)] for j in range(n)]
    crosses = [['.' for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="+" or grid[i][j]=="o":
                pluses[i][j]="+"
            if grid[i][j]=="x" or grid[i][j]=="o":
                crosses[i][j]="x"

    #find crosses to add:
    #first fill in disallowed areas
    for i in range(n):
        for j in range(n):
            if crosses[i][j]=="x":
                rowcols = find_rowcol(i, j, n)
                for r, c in rowcols:
                    if crosses[r][c]==".":
                        crosses[r][c]="/" #no crosses can be in this cell anymore
    for i in range(n):
        for j in range(n):
            if crosses[i][j]==".":
                crosses[i][j]="x"
                rowcols = find_rowcol(i, j, n)
                for r, c in rowcols:
                    if crosses[r][c]==".":
                        crosses[r][c]="/" #no crosses can be in this cell anymore

    #next find pluses to add:
    #first fill in disallowed areas
    for i in range(n):
        for j in range(n):
            if pluses[i][j]=="+":
                diags = find_diag(i, j, n)
                for r, c in diags:
                    if pluses[r][c]==".":
                        pluses[r][c]="/" #no pluses can be in this cell anymore
    #search from parameter in: this should be provably optimal
    #ignore center since never optimal to put a + model in the center (unless grid is size 1)
    for i in range(int(n/2)):
        for j in range(n-2*i-1):
            p = i
            q = j+i
            if pluses[p][q]==".":
                pluses[p][q]="+"
                diags = find_diag(p, q, n)
                for r, c in diags:
                    if pluses[r][c]==".":
                        pluses[r][c]="/" #no pluses can be in this cell anymore
            p = j+i
            q = n-i-1
            if pluses[p][q]==".":
                pluses[p][q]="+"
                diags = find_diag(p, q, n)
                for r, c in diags:
                    if pluses[r][c]==".":
                        pluses[r][c]="/" #no pluses can be in this cell anymore
            p = n-i-1
            q = n-i-j-1
            if pluses[p][q]==".":
                pluses[p][q]="+"
                diags = find_diag(p, q, n)
                for r, c in diags:
                    if pluses[r][c]==".":
                        pluses[r][c]="/" #no pluses can be in this cell anymore            
            p = n-i-j-1
            q = i
            if pluses[p][q]==".":
                pluses[p][q]="+"
                diags = find_diag(p, q, n)
                for r, c in diags:
                    if pluses[r][c]==".":
                        pluses[r][c]="/" #no pluses can be in this cell anymore
    #special case
    if n==1:
        if pluses[0][0]==".":
            pluses[0][0]="+"

    #calculate style points and overall models
    inserted_total = [] #list of the form (r, c, t) where t is type of model
    points = 0
    for i in range(n):
        for j in range(n):
            added_plus = False
            added_cross = False
            if pluses[i][j]=="+":
                points += 1
                if grid[i][j]=="." or grid[i][j]=="x":
                    added_plus = True
            if crosses[i][j]=="x":
                points += 1
                if grid[i][j]=="." or grid[i][j]=="+":
                    added_cross = True
            if not added_plus and not added_cross:
                continue
            elif added_plus and not added_cross and grid[i][j]==".":
                inserted_total.append((i, j, "+"))
            elif not added_plus and added_cross and grid[i][j]==".":
                inserted_total.append((i, j, "x"))
            else:
                inserted_total.append((i, j, "o"))
                
    return points, inserted_total

# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = input().split(" ")
    n = int(n)
    m = int(m)
    grid = [["." for j in range(n)] for k in range(n)]
    for j in range(m):
        t, r, c = input().split(" ")
        grid[int(r)-1][int(c)-1] = t
    points, inserted_total = find_max(grid)
    print("Case #{}: {} {}".format(i, points, len(inserted_total)))
    for j in range(len(inserted_total)):
        print("{} {} {}".format(inserted_total[j][2], inserted_total[j][0]+1, inserted_total[j][1]+1))
