def convertTile(num_rows, num_columns, tile):
    
    current_pos_x = 0
    current_pos_y = 0
    
    while True:
        if tile[current_pos_y][current_pos_x] == '#':
            
            #last column check
            if current_pos_x == num_columns - 1:
                return False
        
            if tile[current_pos_y][current_pos_x + 1] == '#' and \
            not current_pos_y == num_rows - 1 and \
            tile[current_pos_y + 1][current_pos_x] == '#' and \
            tile[current_pos_y + 1][current_pos_x + 1] == '#':
                tile[current_pos_y][current_pos_x] = '/'
                tile[current_pos_y][current_pos_x + 1] = '\\'
                tile[current_pos_y + 1][current_pos_x] = '\\'
                tile[current_pos_y + 1][current_pos_x + 1] = '/'
            else:
                return None
        if current_pos_x < num_columns - 1:
            current_pos_x += 1
        else:
            current_pos_x = 0
            if current_pos_y < num_rows - 1:
                current_pos_y += 1
            else:
                break
    
    return tile

for case in xrange(input()):
    tile_vars = raw_input().split()
    
    tile_rows = int(tile_vars[0])
    tile_columns = int(tile_vars[1])
    
    rows = []
    
    for row in range(tile_rows):
        current_input = raw_input()
        current_row = []
        for char in current_input:
            current_row.append(char)
        rows.append(current_row)
        
    res = convertTile(tile_rows, tile_columns, rows)

    print "Case #%i:" % (case+1)
    if not res:
        print "Impossible"
    else:
        for row in res:
            print "%s" % "".join(row)
