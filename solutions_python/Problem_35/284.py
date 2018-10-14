import sys,os

filename = sys.argv[1].strip()

ifile = open(filename + '.in','r')
all = ifile.readlines()
ifile.close()

ofile = open(filename + '.out','w')

num_maps = int(all[0])
height = 0
width = 0
height_count = 0
maps = []
n = 1
while (n < len(all)):
    line = all[n][:-1]
    vals = line.split(' ')
    while (vals.count('')>0):
        vals.remove('')
    if (height_count>=height):
        height = int(vals[0])
        width = int(vals[1])
        height_count = 0
        maps.append( [] )
        row = 0
        while (row < height):
            maps[-1].append( [] )
            col = 0
            while (col < width):
                maps[-1][-1].append( '' )
                col = col + 1
            row = row + 1
    else:
        m = 0
        while (m < width):
            maps[-1][height_count][m] = int(vals[m])
            m = m + 1
        height_count = height_count + 1
    n = n + 1

letters_large = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def get_neighbors(map,row,col):
    val = map[row][col]
    val_north,val_west,val_east,val_south = (99999,99999,99999,99999)
    if ((row-1)>=0):
        val_north = map[row-1][col]
    if ((col-1)>=0):
        val_west = map[row][col-1]
    if ((col+1)<len(map[row])):
        val_east = map[row][col+1]
    if ((row+1)<len(map)):
        val_south = map[row+1][col]
    return val,val_north,val_west,val_east,val_south


def count_blanks(map):
    counter = 0
    for row in map:
        for val in row:
            if (val==''):
                counter = counter + 1
    return counter

p = 0
for map in maps:
    final = []
    row = 0
    while (row < len(map)):
        final.append( [] )
        col = 0
        while (col < len(map[row])):
            final[-1].append( '' )
            col = col + 1
        row = row + 1
    letter_index = 0

    # Find Sinks
    row = 0
    while (row < len(map)):
        col = 0
        while (col < len(map[row])):
            val,val_north,val_west,val_east,val_south = get_neighbors(map,row,col)
            if (val<=val_north and val<=val_west and val<=val_east and val<=val_south):
                final[row][col] = letters_large[letter_index]
                letter_index = letter_index + 1
            col = col + 1
        row = row + 1

    # Find Other Values
    counter = count_blanks(final)
    while (counter > 0):
        row = 0
        while (row < len(map)):
            col = 0
            while (col < len(map[row])):
                val,val_north,val_west,val_east,val_south = get_neighbors(map,row,col)
                fin,fin_north,fin_west,fin_east,fin_south = get_neighbors(final,row,col)
                if (fin==''):
                    possibles = []
                    finals = []
                    if (val_north<99999 and val_north<val):
                        possibles.append(val_north)
                        finals.append(fin_north)
                    if (val_west<99999 and val_west<val):
                        possibles.append(val_west)
                        finals.append(fin_west)
                    if (val_east<99999 and val_east<val):
                        possibles.append(val_east)
                        finals.append(fin_east)
                    if (val_south<99999 and val_south<val):
                        possibles.append(val_south)
                        finals.append(fin_south)
                    print row,col,val,val_north,val_west,val_east,val_south
                    print possibles
                    min_value = min(possibles)
                    min_index = possibles.index(min_value)
                    fin_value = finals[min_index]
                    final[row][col] = fin_value
                col = col + 1
            row = row + 1
        counter = count_blanks(final)

    # Replace with smart alphabet letters
    replace_what = []
    replace_with = []
    letter_index = 0
    row = 0
    while (row < len(map)):
        col = 0
        while (col < len(map[row])):
            val = final[row][col]
            if (val in letters_large):
                if (val in replace_what):
                    pass
                else:
                    replace_what.append(val)
                    replace_with.append(letters_small[letter_index])
                    letter_index = letter_index + 1
            col = col + 1
        row = row + 1
    row = 0
    while (row < len(map)):
        col = 0
        while (col < len(map[row])):
            val = final[row][col]
            what_index = replace_what.index(val)
            with_value = replace_with[what_index]
            final[row][col] = with_value
            col = col + 1
        row = row + 1
        

    ofile.write('Case #%i:\n' % (p+1))
    print 'Case #%i:' % (p+1)
    for row in final:
        for val in row:
            ofile.write(val + ' ')
            print val,
        ofile.write('\n')
        print

    p = p + 1


ofile.close()
