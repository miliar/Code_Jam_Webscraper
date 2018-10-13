import sys
import math

def generate_successor_states(state, con_flips):
    
    successors = []
    num_possible_actions = len(state) - con_flips + 1
    
    if con_flips > len(state):
        return successors
    
    for i in range(num_possible_actions):
        
        new_state = state[:i]
        
        for j in range(con_flips):
            if state[i+j] == "+":
                new_state = new_state + "-"
            else:
                new_state = new_state + "+"
        
        new_state += state[i+j+1:]
        
        successors.append(new_state)
    
    return successors
        

def findend (start_state, end_state, con_flips, flips):
    
    global states_encountered
            
        
    if flips >= 50:
        return float('inf')
    
    if start_state == end_state:
        return flips
    
        
    successors = generate_successor_states(start_state, con_flips)
    
    if end_state in successors:
        return flips + 1
    else:
        returns = []
        for state in successors:
            
            if state not in states_encountered or states_encountered[state] > flips+1:                
                returns.append(findend (state, end_state, con_flips, flips+1))
                states_encountered[state] = flips+1

    
        if len(returns) == 0:
            return float('inf')
            
        return min(returns)
        
def check_impossible(start_state, end_state, con_flips):
    
    if start_state != end_state and con_flips == len(start_state) - 1:
        return True
    else: 
        return False



if __name__ == "__main__":
    
    
    sys.setrecursionlimit(5000)
    
    
    f = open('A-small-attempt1.in.txt', 'r')
    input = f.read()
    
    #input = "3\n---+-++- 3\n+++++ 4\n-+-+- 4"
    
    lines = input.split('\n')
    
    test_cases = int(lines[0])
    
    for i in range(1, test_cases+1):
        
        case_data = lines[i].split(' ')
        
        start_state = case_data[0]
        con_flips = int(case_data[1])
        
        num_possible_actions = len(start_state) - con_flips + 1
        
        end_state = ["+" for j in range(len(start_state))]
        end_state = ''.join(end_state)
        
        found = False
        
        states_encountered = {}
        
        #if check_impossible(start_state,end_state, con_flips):
        #    print "Case #" + str(i) + ": " + "IMPOSSIBLE"
        #else:
        flips_required = findend (start_state, end_state, con_flips, 0)
        if flips_required == float('inf'):
            print "Case #" + str(i) + ": " + "IMPOSSIBLE"
        else:
            print "Case #" + str(i) + ": " + str(flips_required)

    


