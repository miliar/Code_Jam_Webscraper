import sys
def build_map(lines):
    tmp = []
    for i in lines:
        i = i.strip().split()
        tmp.append([int(j) for j in i])

    return tmp

def check_map(map_array, W, H):
    assert W == len(map_array[0]), 'Map width doesnot match!'
    assert H == len(map_array), 'Map Hight doesnot match!'

def check_direction(map_array, x, y):
    H = len(map_array)
    W = len(map_array[0])

    assert (x < H) and (y < W), 'Coordinate doesnot met dimension: H: %d, W: %d, x: %d, y: %d' % (H, W, x, y)

    cur = map_array[x][y]
    DN = None
    DW = None
    DE = None
    DS = None
    if (x == 0) or (x == (H-1)):
        if H > 1:
            if x == 0:
                DS = cur - map_array[x + 1][y]
            else:
                DN = cur - map_array[x - 1][y]
        if (y != 0) and (y != (W-1)):
            DE = cur - map_array[x][y+1]
            DW = cur - map_array[x][y-1]
        elif y == 0:
            if W > 1:
                DE = cur - map_array[x][y+1]
        elif y == (W-1):
            if W > 1:
                DW = cur - map_array[x][y-1]
        else:
            print "Impossible!!!"
    elif (y == 0) or (y == (W-1)):
        if W > 1:
            if y == 0:
                DE = cur - map_array[x][y+1]
            else:
                DW = cur - map_array[x][y-1]
        if (x != 0) and (x != (H-1)):
            DS = cur - map_array[x+1][y]
            DN = cur - map_array[x-1][y]
        elif x == 0:
            if H > 1:
                DS = cur - map_array[x+1][y]
        elif x == (H-1):
            if H > 1:
                DN = cur - map_array[x-1][y]
        else:
            print "Impossible!!!"
    else:
        DS = cur - map_array[x+1][y]
        DN = cur - map_array[x-1][y]
        DW = cur - map_array[x][y-1]
        DE = cur - map_array[x][y+1]

    value = [DN, DW, DE, DS]
    if (DN <= 0) and (DW <= 0) and (DE <= 0) and (DS <= 0): # this is a sink
        return (x,y)
    else:
        tmp = 0
        index = 999
        for i in range(4):
            if value[i] != None:
                tmp_new = value[i]
                if tmp < tmp_new:
                    index = i
                    tmp = tmp_new

        if index == 0:
            return (x-1,y)
        if index == 1:
            return (x,y-1)
        if index == 2:
            return (x,y+1)
        if index == 3:
            return (x+1, y)
        
        assert False, "Impossible, index = %d" % index

def draw_map(fd, map_array):
    start = ord('a')
    sinks = {}
    H = len(map_array)
    W = len(map_array[0])
    for x in range(H):
        for y in range(W):
            tmp_x = x
            tmp_y = y
            while True:
                (tmp_x2, tmp_y2) = check_direction(map_array, tmp_x, tmp_y)
                if (tmp_x2, tmp_y2) == (tmp_x, tmp_y): # a sink
                    if not ((tmp_x, tmp_y) in sinks.keys()): # a new sink
                        sinks[(tmp_x,tmp_y)] = start + len(sinks.keys())
                    fd.write(chr(sinks[(tmp_x, tmp_y)]))
                    if y < (W-1):
                        fd.write(' ')
                    break
                tmp_x, tmp_y = tmp_x2, tmp_y2
        fd.write('\n')
