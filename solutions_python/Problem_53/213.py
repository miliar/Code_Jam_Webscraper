## -------------------------------------------

def parse_file_A(filename):
    lines = file(filename,'r').read().splitlines()
    counter = 0
    n_cases = map(int, lines[counter].strip().split())[0]
    counter += 1
    cases = []

    for n_case in xrange(n_cases):
        N,K = map(int, lines[counter].strip().split())
        cases.append([N,K])
        counter += 1

    return cases

def solve_case_A(N, K):
    res = (K%(2**N) == (2**N-1))
    return ('ON' if res else 'OFF')
    
    
def print_solution_A(case_number, sol, outfile):
    outfile.write("Case #%d: %s\n" % (case_number+1, sol))
    
    
def solve_A(filename, outfilename):
    cases= parse_file_A(filename)
    outfile = file(outfilename,'w')
    
    for i, x in enumerate(cases):
        print "%d/%d" % (i+1, len(cases))
        n = solve_case_A(x[0], x[1])
        print_solution_A(i, n, outfile)