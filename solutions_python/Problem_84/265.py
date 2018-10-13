from __future__ import division
"""
Code Jam 2011
Round1C: Problem A
"""
import sys

def replace_tiles(tiles):
    r = len(tiles)
    c = len(tiles[0])
    if r >= 2 and c >= 2: # replace only if r,c > 2
        for i in range(0, r - 1):
            for j in range(0, c - 1):
                if tiles[i][j] == tiles[i][j+1] == tiles[i+1][j] == tiles[i+1][j+1] == '#':
                    tiles[i][j] = tiles[i+1][j+1]= '/'
                    tiles[i][j+1] = tiles[i+1][j]= "\\"
    tiles = "\n".join(["".join(r) for r in tiles])

    # now see if there is still any blue tile
    if '#' in tiles:
        return "Impossible"
    else:
        return tiles

def main():
    num_tests = int(sys.stdin.readline())
    for t in range(1, num_tests + 1):
        r, c  = [int(x) for x in sys.stdin.readline().split()]
        tiles = list()
        for i in range(0, r):
            tiles.append(list(sys.stdin.readline().strip()))

        print "Case #%d:" % t
        print replace_tiles(tiles)

if __name__ == '__main__':
    main()
