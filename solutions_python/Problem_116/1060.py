import os
import sys

"""
The basic code for reading a file, should return a string
"""
def parse_input(input_file):
    f = open(input_file, "r")
    final_string = ""
    test_cases = int(f.readline())
    for case in range(test_cases):
        grid = []
        for i in range(4):
            grid.append(list(f.readline()))
            grid[i].pop()
        f.readline()
        done = True
        # Horizontal
        same = False
        found = False
        for i in range(4):
            test = grid[i][0]
            if test == 'T':
                test = grid[i][1]
            same = all(x == test or x == 'T' for x in grid[i])
            if same and test != '.':
                found = True
                final_string = final_string + "Case #{0}: {1} won\n".format(int(case)+1, test)
                break
            if done:
                for mark in grid[i]:
                    if mark == ".":
                        done = False
                        break
        if found:
            continue
        # Vertical
        for i in range(4):
            vert_list = []
            for j in range(4):
                vert_list.append(grid[j][i])
            test = vert_list[0]
            if test == 'T':
                test = vert_list[1]
            same = all(x == test or x == 'T' for x in vert_list)
            if same and test != '.':
                found = True
                final_string = final_string + "Case #{0}: {1} won\n".format(int(case)+1, test)
                break
        if found:
            continue

        # Diagonal
        diagonal_one = []
        diagonal_two = []
        for i in range(4):
            diagonal_one.append(grid[i][i])
            diagonal_two.append(grid[i][len(grid)-i-1])
        test = diagonal_one[0]
        if test == 'T':
            test = diagonal_one[1]
        same = all(x == test or x == 'T' for x in diagonal_one)
        if same and test != '.':
            found = True
            final_string = final_string + "Case #{0}: {1} won\n".format(int(case)+1, test)

        if found:
            continue

        test = diagonal_two[0]
        if test == 'T':
            test = diagonal_two[1]
        same = all(x == test or x == 'T' for x in diagonal_two)
        if same and test != '.':
            found = True
            final_string = final_string + "Case #{0}: {1} won\n".format(int(case)+1, test)

        if found:
            continue

        if done:
            final_string = final_string + "Case #{0}: Draw\n".format(int(case)+1)
        else:
            final_string = final_string + "Case #{0}: Game has not completed\n".format(int(case)+1)

    f.close()
    return final_string

def all_the_same(list):
    for i in range(1,len(list)):
        if list[i-1] != list[i]:
            return False
    return list[0]


"""
Writes a string to the file of the form X-Y-output.txt,
where X is the name of this script and Y is the name of the
test case
"""
def write_output(answer_string):
    script_name = os.path.splitext(sys.argv[0])[0] + "-"
    f = open("Outputs/" + script_name +"output.txt","w")
    f.write(answer_string)
    f.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        answer_string = parse_input(sys.argv[1])
        if answer_string == None:
            print "No answer given"
        else:
            write_output(answer_string)
    else:
        print "Pass in the input file"
