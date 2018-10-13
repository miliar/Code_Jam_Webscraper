import sys

_problem = 'A'

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
        problem_lines.append(line.strip())

    problem_file.close()

    output_file = open(output_filename, 'w')

    print("Solving " + problem_filename)

    Solve(problem_lines, output_file)

    output_file.close()

def Solve(pl, output_file):
    print pl[0]
    definition = map(int,pl[0].split())

    L,D,N = definition

    print "Problem definition " + str(definition)

    SolverInit(pl[1:1+D])

    for casenum in xrange(1,N+1):
        case = pl[D+casenum]
        
        answer = str(SolveCase(case))
        output_file.write("Case #%d: %s\n" % (casenum, answer))
        print("Case #%d: %s" % (casenum, answer))

def SolverInit(initdata):
    global _aliendict
    
    _aliendict = {}

    for word in initdata:
        curdict = _aliendict
        
        for letter in word:
            if letter in curdict:
                curdict = curdict[letter]
            else:
                newdict = {}
                curdict[letter] = newdict
                curdict = newdict

def SolveCase(case):
    global _aliendict
        
    return recursivesolve(case,_aliendict)

def recursivesolve(remains, cdict):
    if remains == '':
        return 1

    if remains[0] == '(':
        matches = 0
        ei = remains.find(')')
        possibs = remains[1:ei]
        leftovers = remains[ei+1:]
        
        for letter in possibs:
            if letter in cdict:
                matches = matches + recursivesolve(leftovers, cdict[letter])
        return matches    
    else:
        letter = remains[0]
        if letter not in cdict:
            return 0
        else:
            return recursivesolve(remains[1:],cdict[letter])
        
