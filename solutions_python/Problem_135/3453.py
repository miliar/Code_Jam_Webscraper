def parse_file(filename):
    # change this
    num = 5
    f = open(filename, "r")
    num_cases = int(f.readline())
    cases = []
    for c in range(num_cases):
        num1 = int(f.readline())
        grid1 = []
        for j in range(4):
            row = f.readline().strip().split(' ')
            grid1.append(row)

        num2 = int(f.readline())
        grid2 = []
        for j in range(4):
            row = f.readline().strip().split(' ')
            grid2.append(row)

        case = (num1, grid1, num2, grid2)
        cases.append(case)

    f.close()
    return cases


def solve_case(case):
    (num1, grid1, num2, grid2) = case
    row1 = set(grid1[num1-1])
    row2 = set(grid2[num2-1])
    overlap = row1.intersection(row2)
    if len(overlap) == 1:
        return overlap.pop()
    elif len(overlap) == 0:
        return "Volunteer cheated!"
    else:
        return "Bad magician!"

def make_output(cases):
    for i in range(len(cases)):
        solution = solve_case(cases[i])
        print "Case #%d: %s" % (i+1, solution) 

def run():
    filename = "A-small-attempt0.in"
    cases = parse_file(filename)
    make_output(cases)

run()

