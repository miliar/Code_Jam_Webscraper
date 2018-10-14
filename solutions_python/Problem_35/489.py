
def calculate_elevations(grid):
    print grid
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print get_surrounding_elevations(x,y,grid)
    return "\n".join([" ".join([str(c) for c in l]) for l in grid])

def get_grids(data):
    num_maps = int(data[0])
    map_position = 1
    grids = []
    for i in range(num_maps):
        grid = []
        num_rows, num_cols = [int(n) for n in data[map_position].strip().split(' ')]
        for l in range(map_position+1,map_position+num_rows+1):
            grid.append([int(n) for n in data[l].split(' ')[0:num_cols]])
        grids.append(grid)
        map_position += num_rows +1
        
    return grids

def is_sink(x,y,grid):
    return all(grid[y][x] > t for t in get_surrounding_elevations(x,y,grid))

def get_lowest_nearby_elevation(x,y,grid):
    minval = [grid[y][x],x,y]
    for delta in [(0,-1),(-1,0),(1,0),(0,1)]:
        sur_x, sur_y = x+delta[0], y+delta[1]
        if sur_x >= 0 and sur_y >=0 and sur_x < len(grid[0]) and sur_y < len(grid):
            if grid[sur_y][sur_x] < minval[0]:
                minval = (grid[sur_y][sur_x], sur_x, sur_y)

    return minval

def get_sink(start_x,start_y,grid):
    x,y = start_x, start_y
    done = False
    count = 0
    while not done and count < 10:
        next = get_lowest_nearby_elevation(x,y,grid)
        if not next:
            return x,y
        count += 1
        x,y = next[1], next[2]
        
    return x,y

def calculate_elevations(grid):
    sinks = {}
    tmp_grid = []
    for row in range(len(grid)):
        tmp_row = []
        for col in range(len(grid[0])):
            sink = get_sink(col,row,grid)
            code = sinks.get(sink)
            if not code:
                code = chr(97+len(sinks))
                sinks[sink] = code
            tmp_row.append(code)
        tmp_grid.append(tmp_row)
    return tmp_grid

if __name__ == "__main__":
    infile = open("B-small.in","r")
    grids = get_grids(infile.readlines())
    outfile = open("watersend.out", "w")
    
    for idx, strgrid in enumerate(["\n".join([" ".join(l) for l in calculate_elevations(grid)]) for grid in grids]):
        outfile.write("Case #%s:\n%s\n" % (idx+1, strgrid))

    outfile.close()

                      
                         
