import sys

def replaceTiles(tiles, i, j):
    if i+1 >= len(tiles) or j+1 >= len(tiles[i]):
        return False
    
    if tiles[i+1][j] != '#' or tiles[i][j+1] != '#' or tiles[i+1][j+1] != '#':
        return False
    
    tiles[i][j] = '/'
    tiles[i][j+1] = '\\'
    tiles[i+1][j] = '\\'
    tiles[i+1][j+1] = '/'
    return True

def main():    
    cases = int(raw_input())
    
    for c in xrange(1, cases+1):
        R, C = map(int, raw_input().split())
        
        tiles = [list(raw_input()) for _ in xrange(R)] 
        
        result = "Impossible"
        replaceOk = True
        for i in xrange(R):
            for j in xrange(C):
                if tiles[i][j] == '#':
                    replaceOk = replaceTiles(tiles, i, j)
                    
                    if not replaceOk: break
            if not replaceOk: break
        
#        print R, C
#        print tiles
        if not replaceOk:
            result = "\nImpossible"
        else:
            result = '\n'+'\n'.join([''.join(i) for i in tiles])
        print "Case #%d: %s"%(c, result)
        #print >> sys.stderr, "Case #%d: %d"%(c, result)
        
if __name__ == '__main__':
    main()
