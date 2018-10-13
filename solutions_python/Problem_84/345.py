#!/usr/bin/python

def is_corner(tile, r, c):
    return (tile[r][c] == '#' and
            tile[r-1][c] != '#' and
            tile[r][c-1] != '#' and
            tile[r+1][c] == '#' and
            tile[r][c+1] == '#' and
            tile[r+1][c+1] == '#')

for case in range(input()):
    R, C = [int(x) for x in raw_input().split()]
    tile = []
    tile.append(list("." * (C + 2)))
    for r in range(R):
        tile.append(list("." + raw_input() + "."))
    tile.append(list("." * (C + 2)))

    corners = []
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if is_corner(tile, r, c):
                corners.append((r, c))
    while corners:
        (r, c) = corners.pop()
        tile[r][c] = '/'
        tile[r][c+1] = '\\'
        tile[r+1][c] = '\\'
        tile[r+1][c+1] = '/'
        if is_corner(tile, r + 2, c + 1):
            corners.append((r + 2, c + 1))
        if is_corner(tile, r + 1, c + 2):
            corners.append((r + 1, c + 2))
        if is_corner(tile, r + 2, c):
            corners.append((r + 2, c))
        if is_corner(tile, r, c + 2):
            corners.append((r, c + 2))

    out = '\n'.join([''.join(row[1:-1]) for row in tile[1:-1]])
    print "Case #%s:" % (case + 1)
    print out if out.find('#') < 0 else 'Impossible'
