#!/usr/bin/env python

from collections import deque

input_file = 'magick-large.dat'

def parse_test_case(line):
    test_deque = deque(line.split())
    
    combinations = {}
    oppositions = {}
    
    # First entry: combinations
    N_comb = int(test_deque.popleft())
    for i in range(0,N_comb):
        comb_str = test_deque.popleft()
        base_pair = comb_str[0:2]
        base_pair_rev = base_pair[::-1]
        compound = comb_str[2]
    
        # Sort of ugly but it's faster to only do the reversing up front    
        combinations[base_pair] = compound
        combinations[base_pair_rev] = compound
    
    # Second entry: oppositions
    N_opp = int(test_deque.popleft())
    for i in range(0,N_opp):
        opp_str = test_deque.popleft()
        
        if (opp_str[0] in oppositions.keys()):
            oppositions[opp_str[0]].add(opp_str[1])
        else:
            oppositions[opp_str[0]] = set( opp_str[1] )

        if (opp_str[1] in oppositions.keys()):
            oppositions[opp_str[1]].add(opp_str[0])    
        else:
            oppositions[opp_str[1]] = set( opp_str[0] )

    # Last entry: invocation
    N_char = int(test_deque.popleft())
    invocation = test_deque.popleft()
    
    return (combinations, oppositions, N_char, invocation)
    

def push_element(element, element_list, combinations, oppositions):
    element_list.append(element)

    # If the list is length 1, nothing else can happen
    if (len(element_list) == 1):
        return element_list
    
    # Check for combinations
    base_pair = element_list[-1] + element_list[-2]
    if(base_pair in combinations.keys()):
        del element_list[-1:-3:-1]
        element_list = push_element(combinations[base_pair], element_list, combinations, oppositions)
        # The recursive call will check for opposition with the new element, so just return here
        return element_list

    # Check for oppositions
    if (element in oppositions.keys()):
        opp_set = oppositions[element]
        opp_found = [ x for x in element_list if x in opp_set ]
        if (opp_found):
            return []

    return element_list

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    for i in range(0,N_tests):
        (combinations, oppositions, N_char, invocation) = parse_test_case(data_file.readline())
        
        element_list = []        
#        print "Invocation: ", invocation
#        print "Combinations: ", combinations
#        print "Oppositions: ", oppositions

        for j in range(0,N_char):
            element_list = push_element(invocation[j], element_list, combinations, oppositions)
#            print element_list
    
        case_str = "Case #%d: %s" % (i+1, element_list)
        print case_str.replace('\'', '')
            
            
            
            