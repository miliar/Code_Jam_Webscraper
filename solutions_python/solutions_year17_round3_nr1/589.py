""" Google Code Jam - Round 1C 2017
    Part A Solution
    Author: Marc Katzef
"""
from math import pi

def solution(in_file):
    """Uses the data in in_file to generate an answer as a single string to be written to file"""
    out_list = []
    
    test_cases = int(in_file.readline().strip())
    
    for i in range(test_cases):
        N, K = map(int, in_file.readline().strip().split())
        pancakes = [] # Each pancake a tuple of (edge area, top area)
        for j in range(N):
            R, H = map(int, in_file.readline().strip().split())
            edge_area = 2 * pi * R * H
            top_area = pi * R ** 2
            pancakes.append((edge_area, top_area, (R, H)))
        
        pancakes.sort()
        rejects = pancakes[:N-K] # discarded
        pancakes = pancakes[N-K:] # give max edge area
        
        if len(rejects) > 0: # could have a base contribute more than worst pancake
            smallest_best = pancakes.pop(0)
            rejects.append(smallest_best)
            
            # find min required radius of base
            max_top = 0
            for edge, top, _ in pancakes:
                if top > max_top:
                    max_top = top
            
            possible_base = (0,0)
            best_contribution = 0
            
            sb_cont = smallest_best[0] + max(0, smallest_best[1] - max_top)
            for edge, top, _ in rejects:
                if top >= max_top: # valid base
                    contribution = (top - max_top) + edge
                    if contribution > sb_cont: # improvement over smallest best
                        if contribution > best_contribution:
                            best_contribution = contribution
                            possible_base = (edge, top, _)
            
            if possible_base == (0,0):
                pancakes.append(smallest_best) # put it back
            else:
                pancakes.append(possible_base) # use improved base
            
        top_area = 0
        edge_area = 0
        for edge, top, _ in pancakes:
            edge_area += edge
            if top > top_area:
                top_area = top
        
        result = edge_area + top_area
        
        out_line = "Case #%d: " %(i+1) + str(result)
        out_list.append(out_line)
    
    return out_list
    

def main():
    """Opens the input file, collects the generated answer and writes it to the output file."""
    input_name = 'A-large.in'
    output_name = input_name + '\'s-output.txt'
    
    in_file = open(input_name)
    out_file = open(output_name, 'w')

    out_list = solution(in_file)
    out_string = '\n'.join(out_list)
    out_file.write(out_string)
    
    in_file.close()
    out_file.close()

    
main()
    

