from math import sqrt, floor, ceil

def check_valid(lawn):
    for i in range(len(lawn)):
        for j in range(len(lawn[0])):
            for k in range(len(lawn)):
                if lawn[i][j] < lawn[k][j]:
                    for l in range(len(lawn[0])):
                        if lawn[i][j] < lawn[i][l]:
                            return "NO"
    return "YES"

name = "B-large"
f = open(name + ".in", "r")
line_num = 0
case_num = 0
curr_case_size = [0,0]
curr_case_line = 0
cases = {}

for line in f:
    line_num += 1
    if line_num == 1:
        continue

    curr_case_line += 1
    if curr_case_size[0] == curr_case_line - 1:
        case_num += 1
        curr_case_size = [int(i) for i in line.strip().split(" ")]
        curr_case_line = 0
        cases[case_num] = []
    else:
        cases[case_num].append([int(i) for i in line.strip().split(" ")])

f.close()

g = open(name + ".out", "w")

for i in range(1, case_num + 1):
    print "Case #" + str(i) + ": " + check_valid(cases[i]) + "\n"
    g.write("Case #" + str(i) + ": " + check_valid(cases[i]) + "\n")

g.close()