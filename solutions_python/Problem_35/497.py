####################################################
#   Tested on python 2.3.5
####################################################

SOUTH = 0
EAST  = 1
NORTH = 2
WEST  = 3


def setdir(char, curdir):
    if (char=='L'):
        curdir = (curdir + 1)%4
    elif (char=='R'):
        curdir = (curdir + 3)%4

    return curdir
        
#fin = open("B-small-attempt0.in", "r")
#fout = open("B-small-practice.out.txt", "w")

fin = open("B-large.in", "r")
#fout = open("B-large-practice.out.txt", "w")

#fin = open("input.txt", "r")
#fout = open("output.txt", "w")

icount = int(fin.readline())
#icount = 1


MAXALT = 99999






for i in range(0,icount):

    listline = fin.readline().split()

    r = int(listline[0])
    c = int(listline[1])

    alts = []
    for j in range(0,r):
        row = map(int, fin.readline().split())
        alts.append(row)

    basins = {}
    curr_basin = 97 #letter a

    basin_map = {}

    for x in range(0,r):
        for y in range(0,c):

            cur = alts[x][y]

            north = west = east = south = MAXALT
            
            if (x>0): north   = alts[x-1][y]
            if (y>0): west    = alts[x][y-1]
            if (y<c-1): east    = alts[x][y+1]
            if (x<r-1): south   = alts[x+1][y]

            minalt = min(north, south, east,west)

            if cur==min(minalt,cur):
                #its a basin
                #basins[(x,y)] = chr(curr_basin)
                #curr_basin += 1
                basin_map[(x,y)]='B'
                #print x,y,basins[(x,y)]
                continue

            if north == minalt:
                basin_map[(x,y)]=(x-1,y)
            elif  west == minalt:
                basin_map[(x,y)]=(x,y-1)
            elif   east == minalt:
                basin_map[(x,y)]=(x,y+1)
            elif   south == minalt:
                basin_map[(x,y)]=(x+1,y)
            else:
                 print "SOMETHING WRONG"


    def getbasin((r1,c1)):
        global curr_basin
        global basins
        global basin_map
        #print "curr_basin", curr_basin
        if basin_map[(r1,c1)]=='B':
            if ((r1,c1)) in basins:
                return basins[(r1,c1)]
            else:
                basins[(r1,c1)] = chr(curr_basin)
                curr_basin += 1
                return basins[(r1,c1)]
        else:
            return getbasin(basin_map[(r1,c1)])
            
##    for y in range(0,c):
##        for x in range(0,r):
##            if basin_map[(x,y)]=='B':
##                basins[(x,y)] = chr(curr_basin)
##                curr_basin += 1

    print "Case #"+str(i+1)+":"
    
    for x in range(0,r):
        for y in range(0,c):
            print getbasin((x,y)),
            #print x,y,"-->",basin_map[(x,y)]
        print



    
    
#    printline = "Case #"+str(i+1)+": " +  + "\n"
#    print printline,
#    fout.write(printline)

fin.close()
#fout.close() 



   



    
        
