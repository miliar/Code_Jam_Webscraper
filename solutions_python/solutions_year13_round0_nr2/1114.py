def possible(lawn,position_x,position_y):
    x_high = True
    for x in range(len(lawn)):
        if (lawn[x][position_y] > lawn[position_x][position_y]):
            x_high = False
			
    y_high = True
    for y in range(len(lawn[0])):
        if (lawn[position_x][y] > lawn[position_x][position_y]):
            y_high = False
    return(y_high or x_high)
	
def check_lawn(lawn):
    for x in range(len(lawn)):
        for y in range(len(lawn[0])):
            if not (possible(lawn, x, y)):
                return(False)
    return(True)

def solve(line):
    lawn = list()
    split = line.split(" ")
    for x in range(int(split[0])):
        split_row = in_file.readline()[:-1].split(" ")
        row = list()
        for y in range(int(split[1])):
            row.append(int(split_row[y]))
        lawn.append(row)
    if (check_lawn(lawn)):
        return("YES")
    else:
        return("NO")
	
def process_tests(command_to_run):
    
    out_file = open("out","w")
    number_of_tests = int(in_file.readline())
    for test_case in range(number_of_tests):
        test_string = in_file.readline()[:-1]
        test_answer = command_to_run(test_string)
        out_file.write("Case #" + str(test_case + 1) + ": " + str(test_answer) + "\n")
    out_file.close()
    in_file.close()
	
in_file = open('in')
process_tests(solve)