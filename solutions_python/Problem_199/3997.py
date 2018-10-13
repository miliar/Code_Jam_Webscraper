def get_test_cases(path_to_file):
    test_cases = []
    with open(path_to_file, 'r') as filestream:
        lines = filestream.readlines()
        num_cases = int(lines[0])
        for line in lines[1:]:
            parts = line.split(' ')
            initial_state = parts[0]
            k = int(parts[1])
            test_cases.append((list(initial_state), k))
    return test_cases

def get_min_flips(initial_state, k):
    #print(initial_state)
    while initial_state:
        pancake = initial_state.pop(0)
        if pancake == '-':
            if k - 1 > len(initial_state):
                return None
            new_state = get_flipped(initial_state[0:(k - 1)]) + initial_state[(k - 1):]
            remaining_flips = get_min_flips(new_state, k)
            if remaining_flips == None:
                return None
            return 1 + remaining_flips
    return 0

def get_flipped(state):
    return ['-' if pancake == '+' else '+' for pancake in state]
