import re, sys

def get_drain_coords(elmap, r, c):
    """Return the (row,col) pair which (r,c) drains to (e.g., lowest tile out of
    adjacent tiles and self)."""
    # define neighbors in priority order: north, west, east, south
    neighbors = [(r-1,c), (r,c-1), (r,c+1), (r+1,c)]
    lowest = (r, c)
    my_height = elmap[r][c]
    min_height = my_height
    for (nr,nc) in neighbors:
        if nr>=0 and nc>=0: # don't wrap-around (too high => exception, so no explicit test)
            try:
                nh = elmap[nr][nc]
                if nh < min_height:
                    min_height = nh
                    lowest = (nr, nc)
            except IndexError:
                pass # ignore out of bounds map check (edge tile)

    return lowest # may be self

def find_sinks(elmap, h, w):
    """Returns a dictionary of sink locations (keys) and drainage sources (values)."""
    # track where each square drains to (intially, every square drains to itself)
    drain_to = [ [(r,c) for c in range(w)] for r in range(h) ]

    # track which squares (directly or indirectly) drain into a given sink
    sinks = {}  # key = (r,c) of sink; value = list of (r,c)'s which drain into it
    for r in range(h):
        for c in range(w):
            x = (r,c)
            sinks[x] = [x] # everything initially is only a sink for itself

    # one-pass: walk over each square and determine where it drains, updating
    # and aggregating sink and drain to lists along the way
    for r in range(h):
        for c in range(w):
            (dr, dc) = get_drain_coords(elmap, r, c)

            # does this tile drain somewhere other than itself?
            if dr != r or dc != c:
                # r,c now drains to dr,dc (and also for anyone sinking into me)
                tiles_with_new_sink = sinks[(r,c)]

                # nobody sinks into r,c anymore
                del sinks[(r,c)]

                # r,c and those sinking into it will sink to dr,dc's sink
                sink_coords = drain_to[dr][dc]
                sinks[sink_coords] += tiles_with_new_sink

                # update back pointers to sink for tiles whose sink changed
                for xr,xc in tiles_with_new_sink:
                    drain_to[xr][xc] = sink_coords

    return sinks

def label_basins(sinks, h, w):
    """Returns a 2-D array of draining basin designations based on the specified
    dictionary of sinks."""
    labels = [ ['?' for c in range(w)] for r in range(h) ]

    # make sure the upper-leftmost tile in the set of sink values is the key
    for sr, sc in sinks.keys():
        key = (sr, sc)
        values = sinks[key]
        mr, mc = min(values)
        mkey = (mr, mc)
        if mkey < key:
            del sinks[key]
            sinks[mkey] = values

    basin_on = 0
    for sr,sc in sorted(sinks.keys()):
        ch = chr(basin_on + ord('a'))
        for r,c in sinks[(sr,sc)]:
            labels[r][c] = ch
        basin_on += 1

    return labels

def main():
    lines = sys.stdin.readlines()
    T = int(lines[0])

    lineOn = 1
    for i in range(T):
        # get the height and width of the map
        params = [int(x) for x in re.findall(r'\d+', lines[lineOn])]
        assert(len(params) == 2)
        lineOn += 1
        H, W = params

        # get the tile heights
        assert(len(lines) >= lineOn + H)
        map_str = ''.join(lines[lineOn:lineOn+H])
        lineOn += H
        elmap = [[int(x) for x in row.split(' ')] for row in map_str.split('\n')[:-1]]
        assert(len(elmap) == H)
        for row in elmap:
            assert(len(row) == W)

        # compute and print the solution
        sinks = find_sinks(elmap, H, W)
        basins = label_basins(sinks, H, W)
        case_num = i + 1
        print 'Case #%u:' % case_num
        for row in basins:
            print ' '.join(row)

main()
