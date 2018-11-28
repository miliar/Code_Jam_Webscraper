
def parse(filepath):
    f = open(filepath)
    cases = []
    test_case_nb = int(f.readline())
    for case_idx in range(test_case_nb):
        cases.append(map(float, f.readline().split()))
    return cases

def solve(cases):
    """
    (C+M)/(2+F*(N+1)) : Time to get M cookie if we buy one more farm
    M/(2+F*N) : Time to get M cookie without buying it

    X/2 : time to get cookies without farms
    C/2 + X/(2+F) : 1 farm, Diff : X/2 < C/2 + X/(2+F)  XF/(2+F) < C
    C/2 + C/(2+F) + X/(2+2F) : ... , Diff: X < C + X(2+F)/(2+2F)| XF/(2+2F) < C
    C/2 + C/(2+F) + C/(2+2F) + X/(2+3F): , X < C + X(2+(N-1)F)/(2+NF)
                                           (XF/C-2)/F < N

    Decision : if XF / (2 + NF) < C then buy a Nth farm
               XF/C < 2 + NF
               (XF/C-2)/F < N

    example: C=500.0, F=4.0 and X=2000.0
    2000*4/6 = 1333 < 500 => buy one farm
    8000/500 - 2 = 14, 14/4 < N => N = 3

    time to buy N farm : C/2 + C/(2+F) + C/(2+2F) ...
    """
    solutions = []
    for case in cases:
        C, F, X = case
        farm_count = int(max(0,(X*F/C-2)/F))
        time = sum([C/(2.+farm_i*F) for farm_i in range(farm_count)]) \
                + X/(2+farm_count*F)
        solutions.append(time)
    return solutions

def write_results(solutions, output_filepath):
    f = open(output_filepath, 'w')
    lines = ["Case #{0}: {1:.7f}".format(solution_idx+1, solution)
             for solution_idx, solution in enumerate(solutions)]
    f.write("\n".join(lines))

if __name__ == '__main__':
    import sys
    cases = parse(sys.argv[1])
    solutions = solve(cases)
    write_results(solutions, sys.argv[2])


