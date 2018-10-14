#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sys

sys.setrecursionlimit(1100)
#sys.maxint
#-sys.maxint-1

def isUsableBlue(tiles, used, i, j):
    if tiles[i][j] == '#' and used[i][j] == '.':
        return True
    return False

def doIt(tiles):
    used = []
    for i in range(len(tiles)):
        used.append(['.']*len(tiles[0]))

    for i in range(len(tiles)):
        for j in range(len(tiles[i])):
            if tiles[i][j] == '#' and used[i][j] == '.':
                if (i < len(tiles)-1 and j < len(tiles[i])-1 and 
                    isUsableBlue(tiles, used, i+1, j) and
                    isUsableBlue(tiles, used, i, j+1) and
                    isUsableBlue(tiles, used, i+1, j+1)):
                    used[i][j] = '/'
                    used[i+1][j] = '\\'
                    used[i][j+1] = '\\'
                    used[i+1][j+1] = '/'
                else:
                    return None
    return used

if __name__ == '__main__':
    f = open(sys.argv[1])

    num_of_case = int(f.readline())
    for t in range(num_of_case):
        n = map(int, f.readline().split())
        R = n[0]
        C = n[1]
        tiles = []
        for i in range(R):
            tiles.append(f.readline().rstrip())

        answer = doIt(tiles)
        print "Case #%d:" % (t+1)
        if answer is None:
            print 'Impossible'
        else:
            for i in range(R):
                print ''.join(answer[i])

# sort by key
# for k,v in sorted(d.items())
# sort by value
# for k,v in sorted(d.items(), key=lambda x:x[1])
# items() return tapple, tapple[0] is k, tapple[1] is v
#
# import copy
# copy.copy()
# copy.deepcopy()
#
# a = [0]*100
#

