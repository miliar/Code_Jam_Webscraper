from sys import argv

def get_one_loop(func, state):
    """get one loop of a repeating function. The first elem of the 
    func's output must be a key that is tested for repetition and 
    the second elem is the state to pass to the next call"""
    seen_keys = dict()
    pattern = []
    while True:
        key, state, out = func(state)
        if key in seen_keys:
            return (pattern[:seen_keys[key]], pattern[seen_keys[key]:])
        seen_keys[key] = len(pattern)
        pattern.append(out)
        

def solve_problem(R, k, N, *g):
    if R == 0: return 0
    g = list(g)
    def get_one_carriage(first_in_line):
        i = first_in_line
        seats = k
        while (i != first_in_line or seats == k) and seats >= g[i]:
            seats -= g[i]
            i = (i + 1) % len(g)
        return (first_in_line, i, k - seats)
    
    #The set of passengers for each carriage is a repeating pattern,
    #so process it in (head, loop*N, tail) sections
    head, loop = get_one_loop(get_one_carriage, 0)
    served = 0
    
    #head
    for car in head:
        served += car
        R -= 1
        if R == 0: return served
    
    #loop
    full_loops = R / len(loop)
    R %= len(loop)
    served += full_loops * sum(loop)
    
    #tail
    for i in xrange(R):
        served += loop[i]
        
    return served
    
def process_file(fin, fout):
    numLines = int(fin.readline())
    for i in range(numLines):
        args = fin.readline().split(' ') + fin.readline().split(' ')
        result = solve_problem(*map(int, args))
        fout.write("Case #%s: %s\n" % (i + 1, result))

process_file(open(argv[1]), open(argv[1].replace("in", "out"), "w"))