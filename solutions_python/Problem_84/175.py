#!/usr/bin/env python

def bluesquare(tiles, x, y):
    if x == len(tiles[0]) -1 or y == len(tiles) - 1:
        return False
    if tiles[y][x] == '#' and tiles[y][x+1] == '#' and \
        tiles[y+1][x] == '#' and tiles[y+1][x+1] == '#':
            return True
    else: return False
    
def setred(tiles, x, y):
    newtiles = []
    for i in range(len(tiles)):
        row = ''
        for j in range(len(tiles[0])):
            if i == y and j == x or i == y + 1 and j == x + 1:
                row += '/'
            elif i == y and j == x + 1 or i == y + 1 and j == x:
                row += '\\'
            else:
                row += tiles[i][j]
        newtiles.append(row)
    return newtiles

def changetiles(tiles):
    for y in range(len(tiles)):
        for x in range(len(tiles[y])):
            if tiles[y][x] == '#':
                if bluesquare(tiles, x, y):
                    newtiles = setred(tiles, x, y)
                    return changetiles(newtiles)
                else:
                    return ['Impossible']
    return tiles

def prettyprint(ar):
    res = '\n'
    for r in ar:
        res += r + '\n'
    return res[:-1]

def main():
    cases = input()
    results = []
    for case in range(cases):
        inp = raw_input()
        inp = inp.split()
        rows = int(inp[0])
        tiles = []
        for r in range(rows):
            tiles.append(raw_input())
        results.append(changetiles(tiles))
    for case in range(cases):
        print 'Case #' + str(case + 1) + ':' + prettyprint(results[case])

if __name__ == '__main__':
    main()