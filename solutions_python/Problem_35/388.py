import sys

L="abcdefghijklmnopqrstuvwxyz"

def findnext(emap, h, w, H, W):
    alt = emap[h][w]
    nexth = h
    nextw = w
    if h > 0 and emap[h-1][w] < alt:
        nexth = h - 1
        nextw = w
        alt = emap[nexth][w]
    if w > 0 and emap[h][w-1] < alt:
        nextw = w - 1
        nexth = h
        alt = emap[h][nextw]
    if w + 1 < W and emap[h][w+1] < alt:
        nextw = w + 1
        nexth = h
        alt = emap[h][nextw]
    if h + 1 < H and emap[h+1][w] < alt:
        nexth = h + 1
        nextw = w
        alt = emap[nexth][w]
    return (nexth, nextw)

def watersheds(infile, no):
    H,W = [int(i) for i in infile.readline().split()]
    emap = []
    for i in range(H):
        emap.append([int(alt) for alt in infile.readline().split()])
    result = [[-1 for j in range(W)] for i in range(H)]
    basin = 0
    for y in range(H):
        for x in range(W):
            cells = []
            h = y
            w = x
            b = -1
            while True:
                if result[h][w] >= 0:
                    b = result[h][w]
                    break
                cells.append((h, w))
                nexth, nextw = findnext(emap, h, w, H, W)
                #print(h,w, nexth,nextw)
                if nexth == h and nextw == w:
                    b = basin
                    basin += 1
                    break
                else:
                    h = nexth
                    w = nextw
            for h,w in cells:
                result[h][w] = b
    print("Case #%d:" % no)
    for row in result:
        for col in row:
            print('%s ' % L[col], end='')
        print()
        
if __name__ == "__main__":
    f = open(sys.argv[1])
    T = int(f.readline())
    for i in range(1, T+1):
        watersheds(f, i)
    f.close()

