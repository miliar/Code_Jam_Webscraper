# Problem B: Magicka

# Read input
    # Build dictionary of combinations
    # Build dictionary of oppositions
    # Build list of inputs
    
# For each element
    # Add to invocation stack
    # While a combination with second-last element is possible, combine
    # If there is an opposition, clear stack
    # Return stack
    
# ------------------------------------------------------------------------------

def read_input(path="B-sample.in"):
    '''
    Read in, process and return the input from the given file.
    '''
    input = open(path).readlines()[1:]
    
    proc = []
    for line in input:
        combos = {}
        oppos = {}
        invoke = []
        line = line.split()
        
        # Get combos
        '''
        combos = {
            E: {A: C, B: D,},
            A: {E: C},
            B: {E: D},
        }
        '''
        combo_len = int(line[0])
        if combo_len > 0:
            for combo in line[1:combo_len+1]:
                if combo[0] not in combos:
                    combos[combo[0]] = {}
                combos[combo[0]][combo[1]] = combo[2]
                if combo[1] not in combos:
                    combos[combo[1]] = {}
                combos[combo[1]][combo[0]] = combo[2]
        line = line[combo_len+1:]
        
        # Get oppos
        '''
        oppos = {
            A: [B, C, D],
            E: [F],
        }
        '''
        oppo_len = int(line[0])
        if oppo_len > 0:
            for oppo in line[1:oppo_len+1]:
                if oppo[0] not in oppos:
                    oppos[oppo[0]] = []
                oppos[oppo[0]].append(oppo[1])
        line = line[oppo_len+1:]
        
        proc.append({'combos': combos, 'oppos': oppos, 'invoke': [c for c in line[1]],})
    return proc

def handle_combinations(elems, combos):
    if len(elems) < 2:
        return elems
        
    if elems[-1] in combos and elems[-2] in combos[elems[-1]]:
        next = elems[:-2] + [combos[elems[-1]][elems[-2]]]
        return handle_combinations(next, combos)
    else:
        return elems
    
def handle_oppositions(elems, oppos):
    if len(elems) < 2:
        return elems
        
    for elem in set(elems):
        if elem in oppos:
            for oppo in oppos[elem]:
                if oppo in elems:
                    return []
    return elems

def solve(input):
    results = []
    out_file = open('b-results.txt', 'wb')
    
    case_num = 1
    for case in input:
        out = []
        for elem in case['invoke']:
            out.append(elem)
            out = handle_combinations(out, case['combos'])
            out = handle_oppositions(out, case['oppos'])
            
        rl = '[%s]' % ', '.join(out)
        r = 'Case #%d: %s' % (case_num, rl)
        out_file.write(r+'\r\n')
        print r
        case_num += 1
        
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    solve(read_input('B-large.in'))