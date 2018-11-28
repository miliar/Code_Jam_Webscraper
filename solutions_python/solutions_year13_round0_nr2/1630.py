input_file = 'B-small-attempt0.in'
output_file = 'B-small-attempt0.out'

# Prepare output to file
open(output_file, 'w').write('')
def print_to_file(line):
    open(output_file, 'a').write(line + '\n')

# Read input
lines = [line.strip() for line in open(input_file, 'r')]

# First element is the number of lawns
total_lawns = lines.pop(0)

# Parse each lawn
lawns = [[]]
lawn_count = 0
lawn_count_temp = -1

for line in lines:

    line = line.split(' ')
    
    # Parse lawn size
    if lawn_count_temp != lawn_count:
        lawn_count_temp = lawn_count
        lawn_line_width = int(line[1])
        lawn_line_count = int(line[0])
        continue  

    if len(line) == lawn_line_width:
        
        # Add line to lawn
        if len(lawns[lawn_count]) < lawn_line_count:
            lawns[lawn_count].append(line)

        # Add new lawn
        if len(lawns[lawn_count]) >= lawn_line_count:
            lawns.append([])
            lawn_count += 1

# Remove last empty lawn
lawns.pop(len(lawns)-1)

def find_path_to_edge(x, y, lawn):

    # Determine size of lawn
    x_length = len(lawn[0])
    y_length = len(lawn)

    # Get square hieght
    height = lawn[y][x]

    path_x_exists = True
    path_y_exists = True
    for i in range(x_length):
        if lawn[y][i] > height:
            path_x_exists = False
            break
    for i in range(y_length):
        if lawn[i][x] > height:
            path_y_exists = False
            break

    return path_x_exists or path_y_exists

i=0
for lawn in lawns:
    i+=1
    result = 'YES'
    for y in range(len(lawn)):
        for x in range(len(lawn[0])):
            if find_path_to_edge(x,y,lawn) == False:
                result = 'NO'
    print_to_file('Case #' + str(i) + ': ' + result)


    

    

