def check_if_possible(floor):
    number_of_blue = 0
    for row in floor:
        number_of_blue += row.count('#')
    if not (number_of_blue % 4) == 0:
        return False
    for row in range(len(floor)-1):
        for tile in range(len(floor[row])-1):
            if floor[row][tile] == '#':
                if not floor[row][tile + 1] == '#':
                    return False
                else:
                    floor[row][tile + 1] = '~'
                if not floor[row + 1][tile] == '#':
                    return False
                else:
                    floor[row + 1][tile] = '~'
                if not floor[row + 1][tile + 1] == '#':
                    return False
                else:
                    floor[row + 1][tile + 1] = '~'
    return True

def change(floor):
    for row in range(len(floor)):
        for tile in range(len(floor[row])):
            if floor[row][tile] == '#':
                floor[row][tile] = '/'
                floor[row][tile + 1] = "\\"
                floor[row + 1][tile] = "\\"
                floor[row + 1][tile + 1] = "/"
    return floor

                 
in_file = open('in')
out_file = open("out","w")
number_of_tests = int(in_file.readline())
for test_case in range(number_of_tests):
    floor = []
    test_string = in_file.readline()[:-1]
    row = int(test_string.split(" ")[0])
    for i in range(row):
        floor.append(list(in_file.readline()[:-1]))
    out_file.write("Case #" + str(test_case + 1) + ":\n")
    if check_if_possible(floor):
        new_floor = change(floor)
        for line in new_floor:
            out_line = ''
            for i in line:
                out_line += i
            out_file.write(out_line + "\n")
    else:
        out_file.write("Impossible\n")
out_file.close()
in_file.close()
