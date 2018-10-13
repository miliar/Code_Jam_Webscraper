def parse_file(filename):
    # change this
    num = 5
    f = open(filename, "r")
    num_cases = int(f.readline())
    cases = []
    for c in range(num_cases):
        row = [float(i) for i in f.readline().strip().split(' ')]
        cases.append(row)

    f.close()
    return cases

def solve(cost, farm_extra, x, num_farms):
    total = 0
    rate = 2
    time = 0
    for i in range(num_farms):
        ttf = cost * 1.0/rate
        time += ttf
        rate += farm_extra
    time += x * 1.0/rate
    return time

def solve_case(case):
    done = False
    num_farms = -1
    (cost, farm_extra, x) = case
    old_time = None
    while True:
        num_farms += 1
        time = solve(cost, farm_extra, x, num_farms)
        if old_time and old_time < time:
            return old_time
        old_time = time


def make_output(cases):
    for i in range(len(cases)):
        solution = solve_case(cases[i])
        print "Case #%d: %s" % (i+1, solution) 

def run():
    #filename = "qualB_in_test.txt"
    filename = "B-small-attempt0.in"
    cases = parse_file(filename)
    make_output(cases)

run()

