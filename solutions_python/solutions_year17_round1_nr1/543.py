import sys

f = sys.stdin
cases = int(f.readline().strip())


# x,y starting indicies
# i,j ending indicies
def fillArr(arr, val, x, y, i, j):
    minrow = min(x, i)
    maxrow = max(x, i)
    mincol = min(y,j)
    maxcol = max(y,j)

    for r in range(minrow, maxrow+1):
        for c in range(mincol,maxcol+1):
            arr[r][c] = val

def improveCell(arr, rows, cols, x, y, hi):
    val = arr[x][y]
    if val == "?": return
    r1 = x
    c1 = y
    r2 = x
    c2 = y
    for i in range(y+1, cols):
        if arr[x][i] == "?" or arr[x][i] == val:
            c2 += 1
        else:
            break
    for i in range(y-1, -1, -1):
        if arr[x][i] == "?" or arr[x][i] == val:
            c1 -= 1
        else:
            break

    # Expand down, if we can
    noGood = False
    for i in range(x+1, rows):
        for j in range(c1, c2+1):
            if arr[i][j] != "?" and arr[i][j] != val:
                noGood = True
                break
        if noGood: break
        r2 += 1

    # Expand up, if we can
    noGood = False
    for i in range(x-1, -1, -1):
        for j in range(c1, c2+1):
            if arr[i][j] != "?" and arr[i][j] != val:
                noGood = True
                break
        if noGood: break
        r1 -= 1

    hi.add(val)
    fillArr(arr, val, r1, c1, r2, c2)

for ii in range(cases):
    line = f.readline().strip().split(" ")
    rows = int(line[0])
    cols = int(line[1])
    haveImproved = set([])

    arr = []

    for i in range(rows):
        l = f.readline().strip()
        arr.append([c for c in l])

    for i in range(rows):
        for j in range(cols):
            if arr[i][j] not in haveImproved:
                improveCell(arr, rows, cols, i, j, haveImproved)

    print "Case #{0}:".format(ii+1)
    for i in range(rows):
        print "".join(arr[i])
