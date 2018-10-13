import fileinput
import copy


def main():
    finput = fileinput.input()
    next(finput)

    caseNb = 1
    for line in finput:
        x, r, c = [int(i) for i in line.split()]
        print "Case #{}: {}".format(caseNb, play(x, r, c))
        caseNb += 1

TILES = [
[[(0, 0)]],
[[(0, 0), (1, 0)]],
[[(0, 0), (1, 0), (2, 0)], [(0, 0), (1, 0), (1, 1)]],
[[(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (2, 0), (2, 1)],
 [(0, 0), (1, 0), (1, 1), (2, 1)], [(0, 0), (1, 0), (2, 0), (1, 1)],
 [(0, 0), (1, 0), (0, 1), (1, 1)]]
]


class grid():
    def __init__(self, r, c):
        self.grid = [[0 for i in xrange(c)] for j in xrange(r)]
        self.r = r
        self.c = c

    def __repr__(self):
        s = ""
        for r in self.grid:
            s += " ".join([str(c) for c in r]) + "\n"
        return s.rstrip()

    def copy(self):
        newGrid = grid(self.r, self.c)
        newGrid.grid = copy.deepcopy(self.grid)
        return newGrid

    def tileFitsAt(self, tile, c, r):
        for unit in tile:
            if (r+unit[1] >= len(self.grid)
                or c+unit[0] >= len(self.grid[0])
                or r+unit[1] < 0 or c+unit[0] < 0):
                    return False
            if self.grid[r+unit[1]][c+unit[0]] != 0:
                return False
        return True

    def placeTileAt(self, tile, c, r):
        for unit in tile:
            self.grid[r+unit[1]][c+unit[0]] = 1
        return self

    def isFull(self):
        for r in xrange(self.r):
            for c in xrange(self.c):
                if self.grid[r][c] != 1:
                    return False
        return True

    def nextPos(self, c, r):
        if c < self.c - 1:
            return (c+1, r)
        if r < self.r - 1:
            return (0, r+1)
        return (None, None)

    def thisTileWins(self, tile, allTiles):
        tileVersions = rotatedTiles(tile)
        tileVersions.extend(rotatedTiles(reflectTile(tile)))
        for r in xrange(self.r):
            for c in xrange(self.c):
                for t in tileVersions:
                    g = grid(self.r, self.c)
                    if g.tileFitsAt(t, c, r):
                        if self.completeTheGame(g.copy().placeTileAt(t, c, r),
                                                allTiles):
                            return False
        return True

    def completeTheGame(self, g, allTiles):
        stack = [[g, 0, (0, 0)]]
        while len(stack) > 0 and len(stack)< 20:
            lst = stack[-1]
            if lst[2][0] is None or lst[2][1] is None:
                stack.pop()
                continue

            if lst[0].isFull():
                return True

            tId, posC, posR = lst[1], lst[2][0], lst[2][1]
            while not lst[0].tileFitsAt(allTiles[tId], posC, posR):
                if tId == len(allTiles) - 1:
                    tId = 0
                    posC, posR = self.nextPos(posC, posR)
                    if posC is None or posR is None:
                        break
                else:
                    tId += 1

            if posC is None or posR is None:
                stack.pop()
                continue

            newG = lst[0].copy().placeTileAt(allTiles[tId], posC, posR)
            stack.append([newG, 0, (0, 0)])
            lst[1] = (tId + 1) % len(allTiles)
            lst[2] = self.nextPos(posC, posR)

        return False


def play(x, r, c):
    tiles = TILES[x-1]
    tileVersions = []
    for idx, tile in enumerate(tiles):
        tileVersions.extend(rotatedTiles(tile))
        if idx > 0 and idx < 4:
            tileVersions.extend(rotatedTiles(reflectTile(tile)))

    g = grid(r, c)

    for tile in tiles:
        if g.thisTileWins(tile, tileVersions):
            return "Richard"
    return "Gabriel"

def rotatedTiles(tile):
    tiles = [tile]
    while len(tiles) < 4:
        newTile = []
        for unit in tiles[-1]:
            newTile.append((-unit[1], unit[0]))
        tiles.append(newTile)
    return tiles

def reflectTile(tile):
    newTile = []
    for unit in tile:
        newTile.append((unit[0], -unit[1]))
    return newTile


main()
