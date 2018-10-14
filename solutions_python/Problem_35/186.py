class Cell:
    def __init__(self, alt, x, y):
        self.alt = alt
        self.x = x
        self.y = y
        self.inbound_links = []
        self.shed = None

T = int(raw_input().strip())

for case in range(T):
    print "Case #%d:" % (case+1)

    H, W = [int(_) for _ in raw_input().strip().split()]
    #print H, W

    map = []
    for y in range(H):
        alts = [int(_) for _ in raw_input().strip().split()]
        cells = []
        for x in range(W):
            cells.append(Cell(alts[x], x, y))
        map.append(cells)

    sinks = []
    for y in range(H):
        for x in range(W):
            # find which direction water will flow from each cell
            cell = map[y][x]
            lowest = None
            for dx, dy in ((0, -1), (-1, 0), (1, 0), (0, 1)):
                xx = x + dx
                yy = y + dy
                if xx >= 0 and yy >= 0 and xx < W and yy < H:
                    poss_dest = map[yy][xx]
                    if lowest is None or poss_dest.alt < lowest.alt:
                        if poss_dest.alt < cell.alt: lowest = poss_dest
            cell.dest = lowest
            if cell.dest is None:
                #print "sink at %d,%d" % (x+1, y+1)
                sinks.append(cell)
            else:
                cell.dest.inbound_links.append(cell)

    # now each cell points to another cell.  cells with dest==None are sinks.
    # so we iterate through the sinks and build watersheds by DFS.
    for sink in sinks:
        nodes = sink.inbound_links[:]
        while len(nodes):
            node = nodes.pop()
            node.sink = sink
            for child in node.inbound_links:
                nodes.append(child)
                
    # now walk through the map and assign letters to sinks while printing them out
    next_letter = 0
    for y in range(H):
        letters = []
        for x in range(W):
            node = map[y][x]
            sink = node.sink if node.dest is not None else node
            if not hasattr(sink, 'letter'):
                sink.letter = chr(ord('a') + next_letter)
                next_letter += 1
            letters.append(sink.letter)
        print " ".join(letters)
