#!/usr/bin/env python

input_file = 'dance-large.dat'
    
def parse_input(input_line):
    input_list = map(int, input_line.split(' '))
    N_goog = input_list[0]
    N_sup = input_list[1]
    p = input_list[2]
    assert len(input_list[3:]) == N_goog
    
    return (N_goog, N_sup, p, sorted(input_list[3:], reverse=True))

with open (input_file, 'r') as data_file:
    N_tests = int(data_file.readline())
    
    for i in range(0, N_tests):
        (N_goog, N_sup, p, score_list) = parse_input(data_file.readline())
        
        pass_count = 0
        marginal_count = 0
        
        for score in score_list:
            (quot, rem) = divmod(score, 3)
            if (rem == 0):
                max = quot
            else:
                max = quot + 1
            
            if (max >= p):
                pass_count += 1
            if (max == p-1 and rem != 1):
                # Surprising scores add one to max if rem = 0 or 2
                # But there are edge cases...
                if (score > 0 and score < 29):
                    marginal_count += 1
                
        if (marginal_count <= N_sup):
            final_count = pass_count + marginal_count
        else:
            final_count = pass_count + N_sup
        
        case_str = "Case #{0:d}: {1:d}".format(i+1, final_count)
        print case_str