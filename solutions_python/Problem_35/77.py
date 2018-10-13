
def Watersheds():
    H, W = map(int, raw_input().split())
    M = []
    alt = []
    for i in range(H):
        M.append([""] * W)
        alt.append(map(int, raw_input().split()))
    count = 0
    for i in range(H):
        for j in range(W):
            path = []
            r, c = i, j
            while not M[r][c]:
                nb = []
                if r > 0:   # N
                    nb.append( (alt[r-1][c], 0, r-1, c) )
                if c > 0:   # W
                    nb.append( (alt[r][c-1], 1, r, c-1) )
                if c < W-1: # E
                    nb.append( (alt[r][c+1], 2, r, c+1) )
                if r < H-1: # S
                    nb.append( (alt[r+1][c], 3, r+1, c) )
                nb.sort()
                if len(nb) == 0 or nb[0][0] >= alt[r][c]:
                    M[r][c] = chr(ord('a')+count)
                    count += 1
                    break
                path.append( (r, c) )
                r, c = nb[0][2:]
            label = M[r][c]
            for r, c in path:
                M[r][c] = label
            print label,
        print

#---------------------------------------------------------------

T = int(raw_input())
for testcase in range(T):
    print "Case #%d:" % (testcase+1)
    Watersheds()
