import sys
import math

def main(args):
    input = open(args[0])
    cases = int(input.readline())
    for i in range(cases):
        casenum = i + 1
        casein = input.readline().split(" ")
        y, x = (int(casein[0]), int(casein[1]))
        tiles = []
        for row in range(y):
            tiles.append(list(input.readline().strip()))
        possible = True
        try:
            for row in range(len(tiles)):
                for tile in range(len(tiles[row])):
                    if(tiles[row][tile] == "#"):
                        tiles[row][tile] = "/"
                        if(not tiles[row+1][tile] == "#"):
                            raise IndexError
                        tiles[row+1][tile] = "\\"
                        if(not tiles[row][tile+1] == "#"):
                            raise IndexError
                        tiles[row][tile+1] = "\\"
                        if(not tiles[row+1][tile+1] == "#"):
                            raise IndexError
                        tiles[row+1][tile+1] = "/"
        except IndexError:
            possible = False
        
        print "Case #{0}:".format(casenum)
        if(possible):
            for row in tiles:
                print "".join(row)
        else:
            print "Impossible"
        

if __name__ == '__main__':
    main(sys.argv[1:])