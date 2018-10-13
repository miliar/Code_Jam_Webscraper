_problem = 'C'

def se():
    problem_filename = _problem + '-example.in'
    output_filename = _problem + '-example.out'

    SolveFile(problem_filename, output_filename)

def SolveSmall():
    problem_filename = _problem + '-small-attempt0.in'
    output_filename = _problem + '-small.out'
    
    SolveFile(problem_filename, output_filename)

def SolveLarge():
    problem_filename = _problem + '-large.in'
    output_filename = _problem + '-large.out'
        
    SolveFile(problem_filename, output_filename)

def SolveFile(problem_filename, output_filename):
    problem_lines = []
    problem_file = open(problem_filename, 'r')

    for line in problem_file:
        problem_lines.append(line)

    problem_file.close()

    output_file = open(output_filename, 'w')

    print("Solving " + problem_filename)

    Solve(problem_lines, output_file)

    output_file.close()

def Solve(pl, output_file):
    print pl[0]
    definition = map(int,pl[0].split())

    N = definition[0]

    print "Problem definition " + str(definition)

    SolverInit(0)

    for casenum in xrange(1,N+1):
        case = pl[casenum]
        
        answer = str(SolveCase(case))
        output_file.write("Case #%d: %s\n" % (casenum, answer))
        print("Case #%d: %s" % (casenum, answer))

def SolverInit(initdata):
    global findstr, indexes

    for i in xrange(len(findstr)):
        if findstr[i] not in indexes:
            indexes[findstr[i]] = []
            
        indexes[findstr[i]].insert(0,i)

findstr = "welcome to code jam"
indexes = {}

def SolveCase(case):
    case = case.strip()
    
    return "%.4d" % (recsolve(case, 0)[0] % 10000)

def recsolve(case,pos):
    global findstr, indexes

    if pos >= len(case):
        empty = [0] * len(findstr)
        empty.append(1)
        return empty

    partial = recsolve(case,pos+1)

    char = case[pos]
    if char in indexes:
        inds = indexes[char]
        for i in inds:
            partial[i] = partial[i] + partial[i+1]
    
    return partial
