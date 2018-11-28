# -*- coding: utf-8 -*-

import sys

def count_blue(picture):
    c = 0
    for line in picture:
        c += len([i for i in line if i == '#'])
    return c

def solve_case(R, C, picture):
    if count_blue(picture) % 4 != 0:
        return 'Impossible'
    for i in range(0, R):
        for j in range(0, C):
            if picture[i][j] == '#':
                if picture[i+1][j] == '#' and\
                    picture[i][j+1] == '#' and\
                    picture[i][j+1] == '#':
                    picture[i][j] = '/'
                    picture[i+1][j] = '\\'
                    picture[i][j+1] = '\\'
                    picture[i+1][j+1] = '/'
                else:
                    return 'Impossible'
    return picture

def read_case(f):
    rc = map(int, f.readline().strip().split())
    picture = []
    for i in range(0, rc[0]):
        picture.append([item for item in f.readline().strip()])
    return [rc[0], rc[1], picture]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        fname = sys.argv[1]
        fin = open(fname)
        fout = open(fname + '.out', 'w')
        T = int(fin.readline().strip())
        idx = 1
        while idx <= T:
            r = solve_case(*read_case(fin))
            fout.write('Case #%s:\n' % idx)
            if isinstance(r, str):
                fout.write('%s\n' % r)
            else:
                for item in r:
                    fout.write('%s\n' % ''.join(item))
            idx += 1
    else:
        print 'Invalid arguments number'
