import os

infile_name = "A-small-attempt0.in"
outfile_name = "A_output.txt"

#state_dict = {}

def output(input_value, i):
    with open(outfile_name,'a') as outfile:
        outfile.write("Case #{0}: {1}\n".format(i, solve(input_value)))
        
def apply_operations(in_dict, states_to_explore, depth, K, goal_state):
    additional_states = []
    for state in states_to_explore:
        new_states = generate_new_states(state, K)
        for n_state in new_states:
            if n_state in in_dict:
                pass
            else:
                if n_state == goal_state:
                    return True
                in_dict[n_state] = depth
                additional_states.append(n_state)
                #print(n_state)
    
    return additional_states
            
    
def generate_new_states(state, K):
    new_states = []
    S = len(state)
    for i in range(0, S-K+1):
        temp_state = modify_state(state, i, i+K)
        new_states.append(temp_state)
        
    return new_states
        
def modify_state(state, lower, upper):
    new_state = list(state)
    for i in range(lower, upper):
        if new_state[i] == '-':
            new_state[i] = '+'
        else:
            new_state[i] = '-'
    return ''.join(new_state)

def solve(input_value):
    S, K = input_value.split(' ')
    K = int(K)
    
    if S == len(S) * '+':
        return 0
    
    #if K not in state_dict:
        #state_dict[K] = {}
        
    current_dictionary = {} #state_dict[K]
    current_dictionary[len(S) * '+'] = 0
    states_to_explore = [len(S) * '+']
    depth = 1
    while(True):
        states_to_explore = apply_operations(current_dictionary, states_to_explore, depth, K, S)
        if states_to_explore == True:
            return depth
        elif states_to_explore == []:
            return "IMPOSSIBLE"
        else:
            depth += 1
    
if __name__ == "__main__":
    if os.path.exists(outfile_name):
        os.remove(outfile_name)
    with open(infile_name, 'r') as infile:
        for i, line in enumerate(infile):
            if i > 0:
                output(line.strip(), i)