
PROBLEM_ID = "A" # A B or C
PROBLEM_SIZE = "small"

def run():
    """
        I/O handler
    """
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)

def solve_case(in_f, out_f, case_index):
    """
        problem solver
    """
    print case_index
    # first time
    line_index1 = int(in_f.readline().rstrip('\n'))
    for x in xrange(line_index1):
        line1 = in_f.readline().rstrip('\n')
    for x in xrange(4 - line_index1):
        in_f.readline().rstrip('\n').split(" ")
    # second time
    line_index2 = int(in_f.readline().rstrip('\n'))
    for x in xrange(line_index2):
        line2 = in_f.readline().rstrip('\n')
    for x in xrange(4 - line_index2):
        in_f.readline().rstrip('\n').split(" ")
    first_4 = line1.split(" ")
    last_4 = line2.split(" ")
    print line1
    print line2
    commons = [x for x in first_4 if x in last_4]
    print commons
    if len(commons) == 1:
        out_f.write("Case #{}: {}\n".format(case_index, commons[0]))
    elif len(commons) == 0:
        out_f.write("Case #{}: {}\n".format(case_index, "Volunteer cheated!"))
    else:
        out_f.write("Case #{}: {}\n".format(case_index, "Bad magician!"))

run()
