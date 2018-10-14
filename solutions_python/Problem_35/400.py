import sys

T = int(sys.stdin.readline())
NUM_MAPS = T

# To solve ties, (y,x)
PREFS = [(-1,0),(0,-1),(0,1),(1,0)]

BASINS = 'abcdefghijklmnopqrstuvwxyz'
basin_idx = 0

def move_dir(y,x,H,W,di):
    ydiff,xdiff = di
    nx = x+xdiff
    ny = y+ydiff
    if nx < 0 or ny < 0 or nx>=W or ny>=H:
        return None
    return (ny,nx)


def flow_dir(data,y,x,H,W):
    mi = data[y][x]
    sdi = None
    for di in PREFS:
        t = move_dir(y,x,H,W,di)
        if t == None:
            continue
        ny,nx = t
        if data[ny][nx] < mi:
            mi = data[ny][nx]
            sdi = di
    return sdi


def find_basin(data, out, y, x, H, W):
    global basin_idx
    
    if out[y][x] != '.':
        return out[y][x]

    di = flow_dir(data, y, x, H, W)
    if di == None:
        out[y][x] = BASINS[basin_idx]
        basin_idx += 1
        return out[y][x]
    ny,nx = move_dir(y,x,H,W,di)
    b = find_basin(data,out,ny,nx,H,W)
    out[y][x] = b
    return b


def do_map(mapnum, H, W):
    global basin_idx
    basin_idx = 0
    data = []
    out = []
    for i in xrange(0, H):
        data.append([int(x) for x in sys.stdin.readline().strip().split()])
        out.append(['.']*W)

    print "Case #%d:" % mapnum

    for y in xrange(0,H):
        for x in xrange(0,W):
            find_basin(data, out, y, x, H, W)

    for l in out:
        print ' '.join(l)
        
    

def main():
    for mapnum in xrange(1,NUM_MAPS+1):
        H,W = map(int,sys.stdin.readline().strip().split())
        do_map(mapnum, H, W)


main()
