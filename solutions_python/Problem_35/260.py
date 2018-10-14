import re

if __name__ == '__main__':
    f = open('c:\\B-large.in')
    fout = open('c:\\result.out', 'w')
    ccase = int(f.readline().strip())
    #print ccase
    for icase in range(ccase):
        H,W=(int(str) for str in f.readline().strip().split())
        #print H,W
        field = []
        basins = []
        for h in range(H):
            altitudes = [int(str) for str in f.readline().strip().split()]
            #print altitudes
            assert(W==len(altitudes))
            line = []
            for w in range(W):
                basin = [(h,w)]
                basins.append(basin)
                line.append([altitudes[w], basin])
            field.append(line)
        #print field
        #print basins
        for h in range(H):
            for w in range(W):
                #print '-----[%d,%d]:%d'%(h,w,field[h][w][0])
                lowest = field[h][w][0]-1
                dir = [None]*4
                if h-1>=0:
                    altitude = field[h-1][w][0]
                    if altitude<=lowest:
                        ##print 'h-1:',altitude
                        dir[0]=(h-1, w)
                        lowest = altitude
                if w-1>=0:
                    altitude = field[h][w-1][0]
                    if altitude==lowest:
                        ##print 'w-1==:',altitude
                        dir[1]=(h, w-1)
                    elif altitude<lowest:
                        ##print 'w-1:',altitude
                        dir[0]=None
                        dir[1]=(h, w-1)
                        lowest = altitude
                if w+1<W:
                    altitude = field[h][w+1][0]
                    if altitude==lowest:
                        ##print 'w+1==:',altitude
                        dir[2]=(h, w+1)
                    elif altitude<lowest:
                        ##print 'w+1:',altitude
                        dir[0]=dir[1]=None
                        dir[2]=(h, w+1)
                        lowest = altitude
                if h+1<H:
                    altitude = field[h+1][w][0]
                    if altitude==lowest:
                        ##print 'h+1==:',altitude
                        dir[3]=(h+1, w)
                    elif altitude<lowest:
                        ##print 'h+1:',altitude
                        dir[0]=dir[1]=dir[2]=None
                        dir[3]=(h+1, w)
                        lowest = altitude
                for d in dir:
                    if not d is None:
                        basin = field[d[0]][d[1]][1]
                        joinbasin = field[h][w][1]
                        if joinbasin[0][0]<basin[0][0] or (joinbasin[0][0]==basin[0][0] and joinbasin[0][1]<basin[0][1]):
                            basin,joinbasin=joinbasin,basin
                        #print basin,
                        basin += joinbasin
                        for h1,w1 in joinbasin:
                            field[h1][w1][1] = basin
                        #print ' join ',joinbasin
                        basins.remove(joinbasin)
                        break
        
        #print basins
        result = [['']*W for i in range(H)]
        for i in range(len(basins)):
            letter = chr(ord('a')+i)
            for h,w in basins[i]:
                result[h][w]=letter
        fout.write('Case #%d:\n'%(icase+1))
        #print 'Case #%d:'%(icase+1)
        for line in result:
            #print line
            for icell in range(len(line)):
                fout.write(line[icell])
                if icell<W-1:fout.write(' ')
            fout.write('\n')
    f.close()
    fout.close()
        