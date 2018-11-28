'''
Created on 2011-05-22

@author: wolf
'''
import sys

test_cases = sys.stdin.read().splitlines()
number_of_cases = int(test_cases[0])
case_index= 0


for test_case in xrange(1, number_of_cases + 1):
    rows_cols = test_cases[case_index + 1].split(" ")
    rows = int(rows_cols[0]) 
    cols = int(rows_cols[1])
    tiles = list()
    
    for row in xrange(0, rows):
        tiles.append(list(test_cases[case_index + 2 + row]))
    
    print "Case #" + str(test_case) + ":"
    for row in xrange(0, rows):
        for column in xrange(0, cols):
            if column + 1 < cols and row + 1 < rows and tiles[row][column] == "#" and tiles[row][column+1] == '#' and tiles[row+1][column] == '#' and tiles[row+1][column+1] == '#': 
                tiles[row][column] = '/'
                tiles[row][column+1] = '\\'
                tiles[row+1][column] = '\\'
                tiles[row+1][column+1] = '/'
                
    if any(map(lambda row: any(map(lambda x: x == "#", row)), tiles)): 
        print "Impossible"
    else:
        print "\n".join(map("".join, tiles))
    case_index += rows + 1