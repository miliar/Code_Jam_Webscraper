DIRECTIONS = (-1, 0), (0, -1), (0, 1), (1, 0)
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def in_range(e_map, row, col):
    return row >= 0 and col >= 0 and row < len(e_map) and col < len(e_map[0])

def find_lowest(e_map, row, col):
    lowest_elevation = e_map[row][col][0]
    lowest_dir = (0, 0)

    for DIR in DIRECTIONS:
        n_row, n_col = row + DIR[0], col +  DIR[1]
        if in_range(e_map, n_row, n_col):
            elevation = e_map[n_row][n_col][0]
            if elevation < lowest_elevation:
                lowest_elevation = elevation
                lowest_dir = DIR

    return lowest_dir

def find_path(e_map, row, col, alphabet_index):
    path = [(row, col)]

    while(True):
        lowest_dir = find_lowest(e_map, row, col)
        if lowest_dir == (0, 0):
            if len(e_map[row][col][1]) > 0:
                name = e_map[row][col][1]
            else:
                name = ALPHABET[alphabet_index]
                alphabet_index += 1
            for coords in path:
                e_map[coords[0]][coords[1]][1] = name
            break
        else:
            row, col = row + lowest_dir[0], col + lowest_dir[1]
            path.append((row, col))

    return alphabet_index

INPUT = open('B-small-attempt0.in')
OUTPUT = open('B-small-attempt0.out', 'w')

T = int(INPUT.readline().strip())

for i in range(T):
    print(i)

    alphabet_index = 0

    #Read map
    H, W = INPUT.readline().split()
    H, W = int(H), int(W)

    e_map = []
    for j in range(H):
        row = INPUT.readline().split()
        for k in range(len(row)):
            row[k] = [row[k], '']
        e_map.append(row)

    #Find basins
    for j in range(len(e_map)):
        for k in range(len(e_map[j])):
            if e_map[j][k][1] == '':
                alphabet_index = find_path(e_map, j, k, alphabet_index)

    #Output map
    print >> OUTPUT, "Case #" + str(i + 1) + ":"
    for row in e_map:
        line = ''
        for cell in row:
            line += cell[1] + ' '
        print >> OUTPUT, line.strip()

INPUT.close()
OUTPUT.close()
