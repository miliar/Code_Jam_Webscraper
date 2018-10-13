#!/usr/bin/python

def result(R, C, tiles):
    for i in range(0, R):
        for j in range(0, C):
            if tiles[i][j] == '#':
                # print i, j
                if j+1 >= C or i+1 >= R:
                    return 'Impossible'
                if tiles[i+1][j] != '#' or tiles[i][j+1] != '#' or tiles[i+1][j+1] != '#':
                    return 'Impossible'
                # print tiles[i][j]
                tiles[i][j] = '/'
                tiles[i][j+1] = '\\'
                tiles[i+1][j] = '\\'
                tiles[i+1][j+1] = '/'
    st = '\n'.join([''.join(x) for x in tiles])
    return st

if __name__ == '__main__':
    T = int(raw_input())
    for k in range(0, T):
        (R, C) = (int(x) for x in raw_input().split())
        tiles = []
        for i in range(0, R):
            tiles.append([x for x in raw_input()])

        print 'Case #' + str(k+1) + ':'
        print result(R, C, tiles)
                    
