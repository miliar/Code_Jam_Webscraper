from copy import deepcopy, copy

class Chest(object):
    def __init__(self, key_for_open, keys_inside):
        self.open = key_for_open
        self.keys = keys_inside
        
    def __repr__(self):
        return 'Chest(open: %d) has (%s)' % (self.open, str(self.keys))

def read_input(filename):
    data = []
    with file(filename, 'rt') as f:
        for line in f:
            data.append(line)
        
    case_num = int(data[0].strip())
	
    cases = []
    curr_line = 1
    for _ in xrange(case_num):
        key_num, chest_num = [int(j) for j in data[curr_line].split()]
        curr_line += 1
        keys = [int(j) for j in data[curr_line].split()]
        keys.sort()
        curr_line += 1
        
        chests = []
        for _ in xrange(chest_num):
            line_nums = [int(j) for j in data[curr_line].split()]
            open_type = line_nums[0]
            keys_inside = line_nums[2:]
            chests.append(Chest(open_type, keys_inside))
            curr_line += 1
        
        cases.append((keys, chests))

    return cases
        
def has_sol(keys, chests):
    # Making list of all keys we still need and what we have
    needed_keys = [chest.open for chest in chests if chest is not None]
    possible_keys = deepcopy(keys)
    
    # Making list of all possible keys to get to
    temp_chests = copy(chests)
    
    changed = True
    while changed:
        changed = False
        for chest in temp_chests:
            if chest is not None and chest.open in possible_keys:
                possible_keys.extend(chest.keys)
                changed = True
                temp_chests.remove(chest)
                
    if any(x is not None for x in temp_chests):
        return False
        
    for key in needed_keys:
        if key not in possible_keys:
            return False
        else:
            possible_keys.remove(key)
            
    return True

def try_solve(keys, chests, solution):
    if all(x is None for x in chests):
        return solution
    
    # Checking if there's even a possible solution
    if not has_sol(keys, chests):
        return []
    
    for (i, chest) in enumerate(chests):
        for key in set(keys):
            # If it has something we need, we try to open it. Otherwise we save our time
            if chest is not None and chest.open == key:
                # Continuing solution
                new_chests = copy(chests)
                new_solution = copy(solution)
                new_keys = copy(keys)
                new_chests[i] = None
                new_solution.append(i+1)
                new_keys.remove(key)
                for new_key in chest.keys:
                    new_keys.append(new_key)
                    
                curr_sol = try_solve(new_keys, new_chests, new_solution)
                
                if curr_sol:
                    return curr_sol
    
    return []
            
def solve_case(case):
    # Getting our data
    keys = case[0]
    chests = case[1]
    solution = []
    
    sol = try_solve(keys, chests, solution)
    
    return sol
    
def get_res(cases):
    # For every case
    res = []
    for i, case in enumerate(cases):
        print i, case
        res.append(solve_case(case))
        
    return res

def create_output(res):
    with file('output1.txt', 'wt') as f:
        for (i, solution) in enumerate(res):
            if solution:
                print >> f, 'Case #%d: %s' % (i + 1, ' '.join([str(j) for j in solution])) 
            else:
                print >> f, 'Case #%d: IMPOSSIBLE' % (i + 1,) 
            
def main():
    import sys
    cases = read_input(sys.argv[1])
    res = get_res(cases)
    create_output(res)

if __name__ == "__main__":
    main()