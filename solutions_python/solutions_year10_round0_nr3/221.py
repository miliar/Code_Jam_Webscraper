## -------------------------------------------

def parse_file(filename):
    lines = file(filename,'r').read().splitlines()
    counter = 0
    n_cases = map(int, lines[counter].strip().split())[0]
    counter += 1
    cases = []

    for n_case in xrange(n_cases):
        n_times, n_people, n_groups = map(int, lines[counter].strip().split())        
        counter += 1
        sizes = map(int, lines[counter].strip().split())        
        counter += 1
        cases.append([n_times, n_people, sizes])


    return cases


def sum(a):
    return reduce(lambda x,y: x+y, a)

def cumsum(a):    
    return [sum(a[:i+1]) for i in range(len(a))]       
            

def solve_case(n_times, n_people, sizes):
    
    next_point = [None]*len(sizes)
    people_in = [None]*len(sizes)
    
    for point in xrange(len(sizes)):
        buffer = sizes[point:]+sizes[:point]
        cb = cumsum(buffer)
        upper = max([i for i in range(len(cb)) if cb[i] <= n_people])        
        next_point[point] = (point+upper+1)%(len(sizes))
        people_in[point] = cb[upper]
        
    total_in = 0
    cur_point = 0
    for n_time in xrange(n_times):
        total_in += people_in[cur_point]
        cur_point = next_point[cur_point]
        
    return total_in
        
    
        
        
    
def print_solution(case_number, sol, outfile):
    outfile.write("Case #%d: %d\n" % (case_number+1, sol))
    
    
def solve(filename, outfilename):
    cases = parse_file(filename)
    outfile = file(outfilename,'w')
    
    for i, x in enumerate(cases):
        print "%d/%d" % (i+1, len(cases))
        n = solve_case(*x)
        print_solution(i, n, outfile)