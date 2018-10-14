#/usr/bin/python
import sys

def substitute_tiles(tiles, rows, columns):
    nblue = 0
    for y in range(rows):
        for x in range(columns):
            if tiles[y][x] == '#':
                nblue += 1
    if nblue % 4:
        return None
    for y in range(rows):
        for x in range(columns):
            if tiles[y][x] == '#':
                if tiles[y+1][x] == '#' and tiles[y][x+1] == '#' and tiles[y+1][x+1] == '#' :
                    tiles[y][x] = '/'
                    tiles[y][x+1] = '\\'
                    tiles[y+1][x] = '\\'
                    tiles[y+1][x+1] = '/'
                else:
                    return None
    return tiles
                    
            
    
           

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(1)
    infile = sys.argv[1]
    outfile = sys.argv[2]
    print infile
    inf = open(infile)
    outf = open(outfile, 'w')
    ncases = int (inf.readline())
    for cnumber in range(ncases):
        headerline = inf.readline()
        rows = int(headerline.split()[0])
        columns = int(headerline.split()[1])
        tiles = {}
        for y in range(rows):
            tiles[y] = list(inf.readline().strip())
        
        tiles = substitute_tiles(tiles, rows, columns)
        outf.write("Case #{0}:\n".format(cnumber+1))
        if tiles:
            for line in tiles:
                outf.write(''.join(tiles[line]))
                outf.write("\n")
        else:
            outf.write("Impossible\n")
    inf.close()
    outf.close()
    
    
    
