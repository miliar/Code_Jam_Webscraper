## -------------------------------------------

def parse_file(filename):
    lines = file(filename,'r').read().splitlines()
    counter = 0
    n_cases = map(int, lines[counter].strip().split())[0]
    counter += 1
    cases = []

    for n_case in xrange(n_cases):
        parts = lines[counter].strip().split()
        pointer = 0
        combines = []
        opposites = []
        for i in range(int(parts[pointer])):
            pointer += 1
            combines.append(parts[pointer])
        pointer += 1
        for i in range(int(parts[pointer])):
            pointer += 1
            opposites.append(parts[pointer])
        pointer += 1
        stack = parts[-1]
        cases.append((combines, opposites, stack))
        
        counter += 1

    return cases

def solve_case(x):
    combines, opposites, stack = x
    dict_combines = {}
    for comb in combines:
        dict_combines[(comb[0], comb[1])] = comb[2]
        dict_combines[(comb[1], comb[0])] = comb[2]
    set_opposites = set([])
    for opp in opposites:
        set_opposites.add((opp[0], opp[1]))
        set_opposites.add((opp[1], opp[0]))
    
    lst = []
    for s in stack:
        lst.append(s)
        while dict_combines.has_key(tuple(lst[-2:])):
            b = lst.pop()
            a = lst.pop()
            lst.append(dict_combines[(a,b)])
        for x in lst[:-1]:
            if (x,lst[-1]) in set_opposites:
                lst = []
                break
    
    return lst
    
    
def print_solution(case_number, sol, outfile):
    sol = '[%s]' % (', '.join(sol))
    outfile.write("Case #%d: %s\n" % (case_number+1, sol))
    
    
def solve(filename, outfilename):
    cases= parse_file(filename)
    outfile = file(outfilename,'w')
    
    for i, x in enumerate(cases):
        print "%d/%d" % (i+1, len(cases))
        n = solve_case(x)
        print_solution(i, n, outfile)