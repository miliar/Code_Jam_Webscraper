## -------------------------------------------

def parse_file(filename):
    lines = file(filename,'r').read().splitlines()
    counter = 0
    n_cases = map(int, lines[counter].strip().split())[0]
    counter += 1
    cases = []

    for n_case in xrange(n_cases):
        counter += 1
        cases.append(map(int, lines[counter].strip().split()))        
        counter += 1

    return cases

def solve_case(x):
    ints = x
    n = len(ints)
    options = [{} for i in range(n)]
    options[0][ints[0]] = [(ints[0], 0)]
    options[0][0] = [(0, ints[0])]
    for i in range(1, n):
        for k,v in options[i-1].iteritems():
            # if add
            options[i][k+ints[i]] = [(w^ints[i],z) for w,z in v]
            # if not
            options[i][k] = [(w,z ^ ints[i]) for w,z in v]

    goods = []
    for k,v in options[n-1].iteritems():
        if k == sum(ints):
            continue
        for w,z in v:
            if w == z:
                goods.append(k) 
    
    if len(goods):
        return str(max(goods))
    else:
        return 'NO'
    
    
def print_solution(case_number, sol, outfile):
    outfile.write("Case #%d: %s\n" % (case_number+1, sol))
    
    
def solve(filename, outfilename):
    cases= parse_file(filename)
    outfile = file(outfilename,'w')
    
    for i, x in enumerate(cases):
        print "%d/%d" % (i+1, len(cases))
        n = solve_case(x)
        print_solution(i, n, outfile)