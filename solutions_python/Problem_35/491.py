file_name = 'B-small-attempt2'
#file_name = 'basin_example'
input = open(file_name + '.in', 'r')
number_of_maps = int(input.readline().strip())
maps =[]
for i in  range(0, number_of_maps):
    (height, width) = input.readline().split()
    print height, width
    map = []
    maps.append(map)
    for r in range(0, int(height)):
        map.append([[int(lat), ''] for lat in input.readline().split()])
print maps
input.close()

map = maps[0]
print map

def move_west(map, r, c):
    if c >  0:
        return map[r][c - 1]
    else:
        return None
def move_north(map, r, c):
    if r >  0:
        return map[r - 1][ c ]
    else:
        return None
def move_south(map, r, c):
    if r<  len(map) - 1:
        return map[r + 1][c]
    else:
        return None
def move_east(map, r, c):
    if c < len(map[0]) - 1:
        return map[r][c + 1]
    else:
        return None
directions = {0:(-1, 0), 1:(0, -1), 2:(0,1), 3:(1,0)}


def find_direction(neighbors, min_neighbor_lat):
   # print neighbors
    for i in range(0, 4):
        if not neighbors[i]:
            continue
        if min_neighbor_lat == neighbors[i][0]:
            return  directions[i]
def find_min_neighbor_lat(neighbors):
    return min([n[0] for n in neighbors if  n])
current_basin_label = ['a']

def move(map, r0, c0, direction):
    r = r0 + direction[0]
    c = c0 + direction[1]
    current_cell = map[r][c]

    print r0, c0, direction, r, c, current_cell
    if current_cell[1]:
        return current_cell[1]
    neighbors = (move_north(map, r, c), move_west(map,r,c), move_east(map, r, c), move_south(map, r, c))
    min_neighbor_lat = find_min_neighbor_lat(neighbors)
    print 'min_neighbor_lat ' + str(min_neighbor_lat), neighbors
    if current_cell[1]:
        return current_cell[1]
    if current_cell[0] <= min_neighbor_lat:
        basin_label = current_basin_label[0]
        current_basin_label[0] = chr(ord(basin_label) + 1)
        if not map[r][c][1]:
            map[r][c][1] = basin_label
            print map
        return basin_label
    else:
        new_direction = find_direction(neighbors, min_neighbor_lat)
        #print new_direction
        basin_label = move(map, r, c, new_direction)
        if not map[r][c][1]: 
            map[r][c][1] = basin_label
            print map
        return basin_label
def solve(map):
    if  len(map) == 1 and len(map[0]) == 1:
        map[0][0][1]='a'
        return map
    for r in range(0, len(map)):
        row = map[r]
        for c in range(0, len(row)):
            move(map, r, c, (0,0))
            #print map[r][c], 
           # print 'neighbors %s, %s, %s, %s' % (move_north(map, r, c), move_west(map, r,c), move_south(map, r,c), move_east(map, r,c))

        print  '\n'
    return map
#move(map, 0, 0, (0,0))

output = open(file_name + '.out', 'w')
for i, map in enumerate(maps):
    test_case_str = 'Case #%d:\n' % (i+1)
    print '===================' + test_case_str
    print map
    output.write(test_case_str)
    current_basin_label = ['a']
    solution = solve(map)
    for r in range(0,len(map)):
        row = map[r]
        output.write(' '.join([cell[1] for cell in row]))
        output.write('\n')
output.close()
           
