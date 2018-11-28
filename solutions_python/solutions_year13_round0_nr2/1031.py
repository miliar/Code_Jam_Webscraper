import os
import sys

"""
The basic code for reading a file, should return a string
"""
def parse_input(input_file):
    f = open(input_file, "r")
    test_cases = int(f.readline())
    final_string = ""
    for case in range(test_cases):
        maxs = {}
        grid = []
        params = f.readline().split()
        n = int(params[0])
        m = int(params[1])
        for i in range(n):
            row = f.readline().split()
            fixed = []
            for height in row:
                fixed.append(int(height))
            grid.append(fixed)
        for i in range(n):
            maxs[('row',i)] = max(grid[i])
        for i in range(m):
            column = []
            for j in range(n):
                column.append(grid[j][i])
            maxs[('column',i)] = max(column)
        found = False
        for i in range(n):
            for j in range(m):
                element = grid[i][j]
                if maxs[('column',j)]  > element and maxs[('row',i)] > element:
                    final_string = final_string + "Case #{0}: NO\n".format(int(case)+1)
                    found = True
                    break
            if found:
                break
        if found:
            continue
        else:
            final_string = final_string + "Case #{0}: YES\n".format(int(case)+1)
    f.close()
    return final_string


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
