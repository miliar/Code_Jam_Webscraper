in_put = open("input.in", 'r')
output = open("output.out", 'w')

test_count = int(in_put.next())

def read_in_lawn(input_stream):
    dimensions = in_put.next().split()
    rows = int(dimensions[0])
    columns = int(dimensions[1])

    lawn = []
    test_lawn = []
    for i in range(0, rows):
        curr_text_line = in_put.next().split()
#        if curr_text_line == "\n":
#            curr_text_line = in_put.next()
            
        lawn.append([])
        test_lawn.append([])
        for j in range(0, columns):
            lawn[i].append(int(curr_text_line[j]))
            test_lawn[i].append(100)
            
    return (lawn, test_lawn, rows, columns)

# returns all requested heights, ordered from largest to smallest
def get_ordered_heights(lawn, rows, columns):
    heights = set([])
    
    for i in range(0, rows):
        for j in range(0, columns):
            heights.add(lawn[i][j])
        
    result = []    
    for height in heights:
        result.append(height)

    result.sort()
    result.reverse()

    return result

# cuts the whole lawn down to the given height
def cut_down(lawn, height):
    for i in range(0, len(lawn)):
        for j in range(0, len(lawn[i])):
            lawn[i][j] = height

def cut_horizontally(template_lawn, test_lawn, height):
    for i in range(0, len(template_lawn)):
        can_cut = True
        for tile in template_lawn[i]:
            if tile > height:
                can_cut = False
                break

        if can_cut:
            for j in range(0, len(template_lawn[i])):
                test_lawn[i][j] = height
                
def cut_vertically(template_lawn, test_lawn, height):
    for column in range(0, len(template_lawn[0])):
        can_cut = True
        for row in range(0, len(template_lawn)):
            if template_lawn[row][column] > height:
                can_cut = False
                break

        if can_cut:
            for row in range(0, len(template_lawn)):
                test_lawn[row][column] = height

for test in range(1, test_count + 1):
    if test > 1:
        output.write("\n")

    (desired_lawn, test_lawn, rows, columns) = read_in_lawn(in_put)

    heights = get_ordered_heights(desired_lawn, rows, columns)

    cut_down(test_lawn, heights[0])

    heights.pop(0)

    for height in heights:
        cut_horizontally(desired_lawn, test_lawn, height)
        cut_vertically(desired_lawn, test_lawn, height)
    
    if test_lawn == desired_lawn:
        output.write("Case #" + str(test) + ": YES")
    else:
        output.write("Case #" + str(test) + ": NO")