""" Google Code Jam - Qualification
    Part C Solution
    Author: Marc Katzef
"""

def get_next_space(N, stalls):
    """A literal interpretation of the brief."""
    ls = {}
    last_left = -1
    for i in range(N):
        if stalls[i]:
            last_left = i
        else:
            ls[i] = i - last_left - 1
    
    rs = {}
    last_right = N
    for i in range(N-1, -1, -1):
        if stalls[i]:
            last_right = i
        else:
            rs[i] = last_right - i - 1

    closest_neighbours = []
    for i in ls:
        closest_neighbours.append((min(ls[i], rs[i]), i))
    
    greatest_min_dist = max(closest_neighbours)[0]
    
    furthest_neighbours = []
    for option in closest_neighbours:
        if option[0] == greatest_min_dist:
            position = option[1]
            f_n_distance = max(ls[position], rs[position])
            furthest_neighbours.append((f_n_distance, position))
    
    greatest_max_dist = max(furthest_neighbours)[0]
    
    possible_indices = [option[1] for option in furthest_neighbours if option[0] == greatest_max_dist]
    choice = min(possible_indices)
    
    return (choice, ls[choice], rs[choice])


def solution(in_file):
    """Uses the data in in_file to generate an answer as a single string to be written to file"""
    out_list = []
    
    test_cases = int(in_file.readline().strip())

    for i in range(test_cases):
        N, K = map(int, in_file.readline().strip().split())
        stalls = [False for j in range(N)]
        
        
        for j in range(K - 1):
            stalls[get_next_space(N, stalls)[0]] = True
        
        choice, left, right = get_next_space(N, stalls)
        out_line = "Case #%d: %d %d" %(i+1, max(left, right), min(left, right))
        out_list.append(out_line)
    
    return out_list
    

def main():
    """Opens the input file, collects the generated answer and writes it to the output file."""
    input_name = 'C-small-1-attempt0.in'
    output_name = 'C\'s-output.txt'
    
    in_file = open(input_name)
    out_file = open(output_name, 'w')

    out_list = solution(in_file)
    out_string = '\n'.join(out_list)
    out_file.write(out_string)
    
    in_file.close()
    out_file.close()

    
main()
    

