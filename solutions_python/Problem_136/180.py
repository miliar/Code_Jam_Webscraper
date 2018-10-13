import datetime
PROBLEM_ID = "B" # A B or C
PROBLEM_SIZE = "large"

def run():
    """
        I/O handler
    """
    start = datetime.datetime.now()
    file_name = "{}-{}".format(PROBLEM_ID, PROBLEM_SIZE)
    in_f = open('{}.txt'.format(file_name), 'r')
    out_f = open('{}.out'.format(file_name), 'w')
    num_of_case = int(in_f.readline().rstrip('\n'))
    print "num of cases:{}".format(num_of_case)
    for i in range(1, num_of_case+1):
        solve_case(in_f, out_f, i)
    finish = datetime.datetime.now()
    print "total seconds:{}".format((finish-start).total_seconds())

def solve_case(in_f, out_f, case_index):
    print case_index
    C, F, X = [float(x) for x in in_f.readline().rstrip('\n').split(" ")]
    P = 2 # initial production rate
    T = 0 # initial time
    result = -1
    while True:
        if C*(P+F) > X*F:
            result = T + X/P
            break
        T = T + C/P
        P = P + F
#        print "#{}:{}".format(times, C/P + X/(P+F) - X/P)
        
    print "{}".format(result)
    out_f.write("Case #{}: {}\n".format(case_index, result))

run()
