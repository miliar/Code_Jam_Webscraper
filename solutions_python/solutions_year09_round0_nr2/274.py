"""
Google Code Jam 2009
Challenge: B. Watersheds

By Marcel Rodrigues

Code for Python 2.5+
"""

inpath = "B-large.in"
outpath = "B-large.out"

def flattree(link, pos, ways=[]):
    if not ways:
        ways = [pos]
    if pos not in link:
        return ways
    ways.extend(link[pos])
    for newpos in link[pos]:
        flattree(link, newpos, ways)
    return ways

infile = open(inpath, "r")
outfile = open(outpath, "w")

T = int(infile.readline().rstrip())

for n in range(T):
    line = infile.readline().rstrip()
    H, W = [int(s) for s in line.split(" ")]
    amap = []
    for y in range(H):
        line = infile.readline().rstrip()
        amap.append([int(s) for s in line.split(" ")])
    # amap index must be amap[y][x]
    link = {}
    sinks = []
    for x in range(W):
        for y in range(H):
            alt = amap[y][x]
            neighbors = []
            if y > 0 and amap[y - 1][x] < alt:
                neighbors.append((y - 1, x))
            if x > 0 and amap[y][x - 1] < alt:
                neighbors.append((y, x - 1))
            if x < W - 1 and amap[y][x + 1] < alt:
                neighbors.append((y, x + 1))
            if y < H - 1 and amap[y + 1][x] < alt:
                neighbors.append((y + 1, x))
            if neighbors:
                flow = min(neighbors, key=lambda pos: amap[pos[0]][pos[1]])
                link[flow] = link.get(flow, []) + [(y, x)]
            else:
                sinks.append((y, x))
    nbasin = {}
    for b in range(len(sinks)):
        flat = flattree(link, sinks[b])
        for pos in flat:
            nbasin[pos] = b
    labels = {}
    curlabel = "a"
    lbasin = {}
    for y in range(H):
        for x in range(W):
            nb = nbasin[(y, x)]
            if nb in labels:
                lbasin[(y, x)] = labels[nb]
            else:
                labels[nb] = curlabel
                lbasin[(y, x)] = curlabel
                curlabel = chr(ord(curlabel) + 1)

    outfile.write("Case #%d:\n" % (n + 1))
    for y in range(H):
        line = ""
        for x in range(W):
            line += lbasin[(y, x)] + " "
        outfile.write(line.rstrip() + "\n")

infile.close()
outfile.close()
