import sys

# Ergh. I thought I'd try out python. It means this is a bit of a mess, because
# I'm not sure of the proper "python" ways of doing things, and I try to apply
# other language paradigms to python. Oh well, it's a good learning experience.

# Alg: Have a 2-dim array representing the map. The data includes the height,
# whether the area has been processed yet, and if so, the drainage basin.
#
# Starting from top left field, have the water flow following the rules until
# it gets to a sink. Then all the fields touched will be sink 'a'. Choose next
# field, and if it has not been touched, have it flow until it finds a sink, or
# it flows to a touched field (an already established drainage basin). If a
# sink, choose the next letter to mark all the touched fields. If a drainage
# basin, mark all touched fields with the letter from the drainage basin.

next_sink = 0

def get_map():
    size = sys.stdin.readline().split()
    size[0] = int(size[0])
    size[1] = int(size[1])

    map = []
    for jj in range(size[0]):
        line = sys.stdin.readline().split()
        map.append([])
        for kk in range(size[1]):
            map[jj].append([int(line[kk]), False, ' '])

    return map

def process_loc(next_x, next_y, map, processed, next_sink):
    if map[next_x][next_y][1] == True:
        for (x, y) in processed:
            map[x][y] = [map[x][y][0], True, map[next_x][next_y][2]]
        return

    # add this location to the list of touched locations
    processed.append((next_x, next_y))

    # find out where the water should flow to
    # first find the lowest surronding location
    # try north
    curr_height = map[next_x][next_y][0]
    low_x = -1
    low_y = -1
    if next_x > 0 and processed.count((next_x-1, next_y)) == 0:
        if map[next_x-1][next_y][0] < curr_height:
            curr_height = map[next_x-1][next_y][0]
            low_x = next_x - 1
            low_y = next_y
    if next_y > 0 and processed.count((next_x, next_y-1)) == 0:
        if map[next_x][next_y-1][0] < curr_height:
            curr_height = map[next_x][next_y-1][0]
            low_x = next_x
            low_y = next_y - 1
    if next_y < len(map[0])-1 and processed.count((next_x, next_y+1)) == 0:
        if map[next_x][next_y+1][0] < curr_height:
            curr_height = map[next_x][next_y+1][0]
            low_x = next_x
            low_y = next_y + 1
    if next_x < len(map)-1 and processed.count((next_x+1, next_y)) == 0:
        if map[next_x+1][next_y][0] < curr_height:
            curr_height = map[next_x+1][next_y][0]
            low_x = next_x + 1
            low_y = next_y

    if low_x < 0:
        # we have a sink!
        for (x, y) in processed:
            map[x][y] = [map[x][y][0], True, next_sink[0][next_sink[1]]]
        next_sink[1] = next_sink[1] + 1
    else:
        # process next location
        process_loc(low_x, low_y, map, processed, next_sink)

    
def process_map(map):
    next_x = 0
    next_y = 0
    
    sink_names = ["abcdefghijklmnopqrstuvwxyz", 0]

    while next_x < len(map) and next_y < len(map[0]):
        process_loc(next_x, next_y, map, [], sink_names)

        next_y = next_y + 1
        if next_y >= len(map[0]):
            next_x = next_x + 1
            next_y = 0

    for ii in range(len(map)):
        for jj in range(len(map[ii])-1):
            print(map[ii][jj][2], " ", end='') 
        print(map[ii][len(map[ii])-1][2])

# Main code:
num_of_maps = int(sys.stdin.readline())

for ii in range(num_of_maps):
    map = get_map()
    print("Case #" + str(ii+1) + ":")
    process_map(map)
