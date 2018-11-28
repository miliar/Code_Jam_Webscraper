# Mallin Moolman

filename = "B-large.in"
f = open (filename)
outfile = open (filename.rsplit(".", 1)[0] + ".out", 'w')

t = int(f.readline().strip())

for mapno in xrange(t):
    letters = [chr(i) for i in xrange(96+26, 96, -1)]
    
    h, w = [int(x) for x in f.readline().strip().split(" ")]

    maplist = []
    for lineno in xrange(h):
        maplist.append ([int(x) for x in f.readline().strip().split(" ")])

    vectors = [[() for i in xrange(w)] for j in xrange(h)]
    basins = [[None for i in xrange(w)] for j in xrange(h)]
    for i in xrange(h):
        for j in xrange(w):
            adjalts = []
            lowestalt = maplist[i][j]
            lowestpoint = (i, j)
            for di, dj in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
                if 0 <= i+di < h and 0 <= j+dj < w:
                    if maplist[i+di][j+dj] < lowestalt:
                        lowestalt = maplist[i+di][j+dj]
                        lowestpoint = (i+di, j+dj)

            vectors[i][j] = lowestpoint


    def basinval (point):
        if basins[point[0]][point[1]] is None:
            
            if vectors[point[0]][point[1]] == point:
                basins[point[0]][point[1]] = letters.pop()
                return basins[point[0]][point[1]]
            else:
                return basinval(vectors[point[0]][point[1]])
        else:
            return basins[point[0]][point[1]]
        
        

    for i in xrange(h):
        for j in xrange(w):
            if basins[i][j] is None:
                basins[i][j] = basinval ((i, j))

       
    outfile.write( ("Case #%d:\n" % (mapno+1)) + "\n".join([" ".join(line) for line in basins]) + "\n")
    

f.close()
outfile.close()
