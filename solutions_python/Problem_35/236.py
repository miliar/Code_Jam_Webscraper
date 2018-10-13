import sys
t = int(sys.stdin.readline().strip())

moo = "abcdefghijklmnopqrstuvwxyz"

def go(r, c):
    global map, label, h, w, l
    if label[r][c] != None:
        return label[r][c]
    best = (map[r][c], r, c)
    if r > 0 and map[r-1][c] < best[0]:
        best = (map[r-1][c], r-1, c)
    if c > 0 and map[r][c-1] < best[0]:
        best = (map[r][c-1], r, c-1)
    if c < w-1 and map[r][c+1] < best[0]:
        best = (map[r][c+1], r, c+1)
    if r < h-1 and map[r+1][c] < best[0]:
        best = (map[r+1][c], r+1, c)
    if best[1] == r and best[2] == c:
        label[r][c] = moo[l]
        l += 1
    else:
        label[r][c] = go(best[1], best[2])
    return label[r][c]

for x in range(t):
    temp = [int(z) for z in sys.stdin.readline().strip().split()]
    h, w = temp[0], temp[1]
    map = [[int(z) for z in sys.stdin.readline().strip().split()] for y in range(h)]
    label = [[None for y in range(w)] for z in range(h)]
    l = 0
    for r in range(h):
        for c in range(w):
            go(r, c)
    print "Case #%d:" % (x + 1)
    print "\n".join(" ".join(row) for row in label)

