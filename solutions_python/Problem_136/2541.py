"""
cookie clicker
https://code.google.com/codejam/contest/2974486/dashboard#s=p1
"""
def ParseCases(text):
    """splits the string and outputs required matrices"""
    lines = text.splitlines()
    num_cases = int(lines[0])
    C = [] # buy farm thres
    F = [] # rate increaser for each farm bought
    X = [] # target
    line_index = 1
    for i in range(num_cases):
        line = lines[line_index].split()
        #print line
        C.append(float(line[0]))
        F.append(float(line[1]))
        X.append(float(line[2]))
        line_index += 1
    return {'numCases': num_cases, 'C': C,'F': F,'X': X}

def SolveCase(C, F, X):
    """
    solves the cookie clicker case and
    returns the minimum time to solution
    """
    rate = 2
    time_offset = 0
    target = X
    farm_get_val = C
    farmget_time_seq = []  # time taken with diff strategy to reach farm getting value
    target_time_seq = []  # time taken with diff strategy to reach target value

    while True:
        farm_get_time = time_offset + (farm_get_val / float(rate))
        target_time = time_offset + (target / float(rate))

        farmget_time_seq.append(farm_get_time)
        target_time_seq.append(target_time)

        rate += F
        time_offset = farm_get_time

        if len(target_time_seq) > 1:
            if target_time_seq[-1] > target_time_seq[-2]:
                break

    return target_time_seq[-2]


if __name__ == "__main__":
    # parse input file
    inp_file_name = 'B-large.in'
    out_file_name = 'B-large.out'
    with open(inp_file_name, 'rb') as inp:
        cases = ParseCases(inp.read())
        # find sequence of total times for each function chosen
        for index in range(cases["numCases"]):
            C = cases["C"][index]
            F = cases["F"][index]
            X = cases["X"][index]
            best_time = SolveCase(C, F, X)
            with open(out_file_name, 'a') as out:
                out.write("Case #{i}: {ans:.{digits}f}\n".format(i = index + 1, ans = best_time, digits = 7))



