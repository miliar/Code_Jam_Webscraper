from sys import stdin

def replace(pic, row, col, tile):
    if row >= len(pic): return False
    if col >= len(pic[row]): return False
    if (pic[row][col] != "#"): return False
    pic[row][col] = tile
    return True

for case in range(1, int(stdin.readline()) + 1):
    (r, c) = (int(x) for x in stdin.readline().split())
    p = []
    for i in range(r): p.append([x for x in stdin.readline().strip()])

    success = True

    for i in range(r):
        if (not success): break
        for j in range(c):
            if p[i][j] == "#":
                success = replace(p, i, j+1, "\\")
                success &= replace(p, i+1, j, "\\")
                success &= replace(p, i+1, j+1, "/")
                if (success):
                    p[i][j] = "/"
                else:
                    break;

    print "Case #%d:" % case
    if (not success):
        print "Impossible"
    else:
        for prow in p:
            print "%s" % ''.join(prow)
