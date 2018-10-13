## -------------------------------------------

# http://numpy.scipy.org/
# from numpy import *



def parse_file(filename):
    lines = file(filename,'r').read().splitlines()
    counter = 0
    n_cases = map(int, lines[counter].strip().split())[0]
    counter += 1
    cases = []

    for n_case in xrange(n_cases):
        N,K = map(int, lines[counter].strip().split())
        counter += 1
        
        board = []
        for row in xrange(N):
            board.append(lines[counter].strip())
            counter += 1
            
        cases.append([board,N,K])
        

    return cases

def solve_case(x):
    board, N, K = x
    
    # first turn the board
    turned = []
    for line_n in range(N):        
        newline = []
        added = 0
        for c in board[line_n][::-1]:
            if c in 'RB':
                newline.append(c)
                added += 1
        newline += ['.']*(N-added)
        newline = newline[::-1]
        turned.append(newline)
    turned = turned[::-1]
    trans = [[turned[j][i] for j in range(N)] for i in range(N)]
    
    print '\n'.join([''.join(x) for x in turned])
    print '\n'*2
    print '\n'.join([''.join(x) for x in trans])
    
    blue = False
    red = False
    # look for horizontals
    for i in range(N):
        cat = ''.join(trans[i])
        print cat
        if 'B'*K in cat:
            blue = True
        if 'R'*K in cat:
            red = True
            
    print 
            
    # look for verticals
    for i in range(N):
        cat = ''.join(turned[i])
        print cat
        if 'B'*K in cat:
            blue = True
        if 'R'*K in cat:
            red = True
            
    print 
    
    # horiz:
    for i in range(N):
        cat = ''.join([trans[i+j][j] for j in range(N-i)])
        print cat
        if 'B'*K in cat:
            blue = True
        if 'R'*K in cat:
            red = True
            
    print
    for i in range(N):        
        cat = ''.join([trans[j][i+j] for j in range(N-i)])
        print cat
        if 'B'*K in cat:
            blue = True
        if 'R'*K in cat:
            red = True
            
    print
    
    # horiz:
    for i in range(N):
        cat = ''.join([turned[i+j][j] for j in range(N-i)])
        print cat
        if 'B'*K in cat:
            blue = True
        if 'R'*K in cat:
            red = True
            
    print 
    for i in range(N):       
        cat = ''.join([turned[j][i+j] for j in range(N-i)])
        print cat 
        if 'B'*K in cat:
            blue = True
        if 'R'*K in cat:
            red = True
            
    print
            
    if blue and red:
        return 'Both'
    if blue and not red:
        return 'Blue'
    if not blue and red:
        return 'Red'
    if not blue and not red:
        return 'Neither'
        
            
    
    
    
def print_solution(case_number, sol, outfile):
    outfile.write("Case #%d: %s\n" % (case_number+1, sol))
    
    
def solve(filename, outfilename):
    cases= parse_file(filename)
    outfile = file(outfilename,'w')
    
    for i, x in enumerate(cases):
        print "%d/%d" % (i+1, len(cases))
        n = solve_case(x)
        print_solution(i, n, outfile)