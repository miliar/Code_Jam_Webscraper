class point:
    def __init__(self, r, c, value):
        self.r = r
        self.c = c
        self.value = value
        self.basin = 0
    def __repr__(self):
        return "<point: r = " + str(self.r) + ", c = " + str(self.c) + ", value = " + \
            str(self.value) + ", basin = " + str(self.basin) + ">"

def getLower(p, map, H, W):
    value = p.value
    lower = p
    for (offR, offC) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        (r2, c2) = (p.r + offR, p.c + offC)
        if r2 >= 0 and r2 < H and c2 >= 0 and c2 < W:
            if map[r2][c2].value < value:
                lower = map[r2][c2]
                value = map[r2][c2].value
    return lower

def findSinks(map, H, W):
    sinks = []
    basin = 1
    for row in map:
        for p in row:
            sink = getLower(p, map, H, W)
            if p == sink:
                p.basin = basin
                basin += 1
                sinks.append(p)
    return sinks

def relabelBasins(map):
    labels = {}
    nextLabel = 'a'
    for row in map:
        for p in row:
            if labels.has_key(p.basin):
                p.label = labels[p.basin]
            else:
                p.label = labels[p.basin] = nextLabel
                nextLabel = chr(ord(nextLabel) + 1)

def flood(p, map, H, W):
    for (offR, offC) in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
        (r2, c2) = (p.r + offR, p.c + offC)
        if r2 >= 0 and r2 < H and c2 >= 0 and c2 < W and map[r2][c2].basin == 0 and \
            getLower(map[r2][c2], map, H, W) == p:
            map[r2][c2].basin = p.basin
            flood(map[r2][c2], map, H, W)

infile = open("../B-large.in", "r")
outfile = open("../B-large.out", "w")
T = int(infile.readline().strip())
for testcaseN in range(T):
    (H, W) = [int(n) for n in (infile.readline().split())]
    map = []
    r = 0
    for line in range(H):
        c = 0
        row = []
        for entry in infile.readline().split():
            row.append(point(r, c, int(entry)))
            c += 1
        map.append(row)
        r += 1
    sinks = findSinks(map, H, W)
    for sink in sinks:
        flood(sink, map, H, W)
    relabelBasins(map)
    outfile.write("Case #" + str(testcaseN + 1) + ":\n")
    outfile.write("\n".join([" ".join([p.label for p in row]) for row in map]) + "\n")