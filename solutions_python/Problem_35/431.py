#google code jam '09 template
#


file_name = 'B-small-attempt0.in'
read_fp = None

land = []
drain = []

def main():
    global file_name
    global land
    global drain
    read_fp = open(file_name)


    num_maps = int(read_fp.readline().strip())

    for m in range(num_maps):
        basin = 'A'
        land = []
        dim = read_fp.readline().strip().split(' ')
        dim[0] = int(dim[0])
        dim[1] = int(dim[1])
        drainmap(dim)
        for i in range(dim[0]):
            row = read_fp.readline().strip().split()
            for k in range(len(row)):
                row[k] = int(row[k])
            land += [row]

        #locate sinks
        for i in range(dim[0]):
            for j in range(dim[1]):
                if isSink([i,j]):
                    drain[i][j] = basin
                    #print "%i,%i is sink"%(i,j),basin
                    basin = chr(ord(basin)+1)
                    
        #find corresponding sink
        for i in range(dim[0]):
            for j in range(dim[1]):
                drain[i][j] = findSink([i,j])

        #rearrange labels
        translate_dict = {}
        basin = 'a'
        for i in range(dim[0]):
            for j in range(dim[1]):
                if drain[i][j] not in translate_dict.keys():
                    #add new dict entry
                    translate_dict[drain[i][j]] = basin
                    #increment basin
                    basin = chr(ord(basin)+1)
                    #replace label
                    drain[i][j] = translate_dict[drain[i][j]]
                else:
                    #replace label
                    drain[i][j] = translate_dict[drain[i][j]]

        #print
        print "Case #%i:"%(m+1)
        for i in range(dim[0]):
            for j in range(dim[1]):
                print drain[i][j],
            print ''
            
    
    return

def isSink(coor):
    global land
    alt = land[coor[0]][coor[1]]
    nalt = altitude(coor,'n')
    salt = altitude(coor,'s')
    walt = altitude(coor,'w')
    ealt = altitude(coor,'e')
    if alt <= nalt and \
       alt <= salt and \
       alt <= ealt and \
       alt <= walt:
        return True
    else:
        return False


def findSink(coor):
    global sink
    global land
    alt = land[coor[0]][coor[1]]
    sink_dir = None
    lowest = alt
    if isSink(coor):
        return drain[coor[0]][coor[1]]
    for direction in ['s','e','w','n']:
        if altitude(coor,direction) > lowest:
            pass
        else:
            lowest = altitude(coor,direction)
            sink_dir = direction
    if sink_dir == None:
        return -1
    else:
        ncoor = neighbour(coor,sink_dir)
        if ncoor:
            return findSink(neighbour(coor,sink_dir))
        else:
            print "ERROR:",coor,sink_dir
            print land
    



def neighbour(coor,direction):
    global land
    if direction == 'n':
        if coor[0] <= 0:
            return False
        else:
            return [coor[0]-1,coor[1]]
    elif direction == 's':
        if coor[0] >= len(land)-1:
            return False
        else:
            return [coor[0]+1,coor[1]]
    elif direction == 'e':
        if coor[1] >= len(land[0])-1:
            return False
        else:
            return [coor[0],coor[1]+1]
    elif direction == 'w':
        if coor[1] <= 0:
            return False
        else:
            return [coor[0],coor[1]-1]
    else:
        return False


def altitude(coor,direction):
    global land
    if direction == 'n':
        if coor[0] <= 0:
            return 999
        else:
            return land[coor[0]-1][coor[1]]
    elif direction == 's':
        if coor[0] >= len(land)-1:
            return 999
        else:
            return land[coor[0]+1][coor[1]]
    elif direction == 'e':
        if coor[1] >= len(land[0])-1:
            return 999
        else:
            return land[coor[0]][coor[1]+1]
    elif direction == 'w':
        if coor[1] <= 0:
            return 999
        else:
            return land[coor[0]][coor[1]-1]
    else:
        return False
    
def drainmap(dim):
    global drain
    drain = []
    for i in range(dim[0]):
        drain += [[]]
        for j in range(dim[1]):
            drain[i] += [0]


if (__name__ == "__main__"):
    main()
