import sys;
import re;

MAX_ALT = 10000;

numSinks = 0;

def start(x, y, W, H, grid, dirGrid):
    global numSinks;
    if dirGrid[y][x] != -1:
        return dirGrid[y][x];

    #if dirGrid[y][x] == -2:
    #    dirGrid[y][x] = numSinks;
    #    numSink = numSinks + 1;
    #    return dirGrid[y][x];

    #dirGrid[y][x] = -2;

    # [N, W, S, E];
    neighbors = [MAX_ALT+1, MAX_ALT+1, MAX_ALT+1, MAX_ALT+1];
    if y > 0:
        neighbors[0] = grid[y-1][x];
    if x > 0:
        neighbors[1] = grid[y][x-1];
    if y < H-1:
        neighbors[2] = grid[y+1][x];
    if x < W-1:
        neighbors[3] = grid[y][x+1];

    m = min(neighbors);
    if grid[y][x] <= m:
        dirGrid[y][x] = numSinks;
        numSinks = numSinks + 1;
    else:
        nextX = x; nextY = y;
        if neighbors[0] == m: # north
            nextY = y-1;
        elif neighbors[1] == m: # west
            nextX = x-1;
        elif neighbors[3] == m: # east
            nextX = x+1;
        elif neighbors[2] == m: #south
            nextY = y+1;

        dirGrid[y][x] = start(nextX, nextY, W, H, grid, dirGrid);

    return dirGrid[y][x];


def solve(H, W, grid):

    dirGrid = []
    for y in xrange(H):
        sinks = []
        for x in xrange(W):
            sinks.append(-1);
        dirGrid.append(sinks);

    for y in xrange(H):
        for x in xrange(W):
            start(x, y, W, H, grid, dirGrid);

    sinkMap = {};

    alpha = "abcdefghijklmnopqrstuvwxyz";
    nextChar = 0;
    result = "";
    for y in xrange(H):
        for x in xrange(W):
            if not sinkMap.has_key(dirGrid[y][x]):
                sinkMap[dirGrid[y][x]] = alpha[nextChar];
                nextChar = nextChar + 1;
            basin = sinkMap[dirGrid[y][x]];   
            result += basin + " ";
        result += "\n";

    return result;

out = open(sys.argv[2], "w");
f = open(sys.argv[1]);
T = int(f.readline());

for i in xrange(T):
    line = f.readline();
    vals = map(int, line.split(' '));
    H = vals[0]; W = vals[1];

    grid = [];
    for y in xrange(H):
        grid.append(map(int, f.readline().split(' ')));

    result = solve(H, W, grid);
    out.write("Case #%d:\n" % (i+1));
    out.write(result);

out.close();
