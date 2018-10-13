from numpy import array, zeros_like
from copy import copy
INF = float('infinity')

infile = open("B-large.in","r")
outfile = open("B-large.out","w")
numcases = int(infile.readline().strip())

for case in range(numcases):
    HW = infile.readline().strip().split(" ")
    H = int(HW[0])
    W = int(HW[1])
    Ha = H-1
    Wa = W-1
    listmap = []
    for y in range(H):
        newrow = []
        inrow = infile.readline().strip().split(" ")
        for x in inrow:
            newrow.append(int(x))
        listmap.append(newrow)
    altmap = array(listmap)
    basinmap = zeros_like(altmap)

    next_basin = 1
    for starty in range(H):
        for startx in range(W):
            path = []
            if basinmap[starty,startx] != 0:
                continue
            y = copy(starty)
            x = copy(startx)
            while basinmap[y,x] == 0:
                path.append((y,x))
                a_here = altmap[y,x]
                if y == 0:
                    a_N = INF
                else:
                    a_N = altmap[y-1,x]
                if x == 0:
                    a_W = INF
                else:
                    a_W = altmap[y,x-1]
                if x == Wa:
                    a_E = INF
                else:
                    a_E = altmap[y,x+1]
                if y == Ha:
                    a_S = INF
                else:
                    a_S = altmap[y+1,x]
                if a_here<=a_N and a_here<=a_W and a_here<=a_E and a_here<=a_S:
                    #Sink
                    for point in path:
                        basinmap[point] = next_basin
                    next_basin += 1
                    break
                elif a_S<a_N and a_S<a_W and a_S<a_E:
                    y += 1
                elif a_E<a_N and a_E<a_W:
                    x += 1
                elif a_W<a_N:
                    x -= 1
                else:
                    y -= 1
            else:
                # Join into another basin
                join_basin = basinmap[y,x]
                for point in path:
                    basinmap[point] = join_basin
    out = "Case #" + str(case+1) + ":\n"
    for row in basinmap:
        outrow = []
        for col in row:
            outrow.append(chr(col+96))
        out += " ".join(outrow) + "\n"
    print out
    outfile.write(out)

infile.close()
outfile.close()
