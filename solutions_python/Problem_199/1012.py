""" Google Code Jam - Qualification
    Part A Solution
    Author: Marc Katzef
"""

def are_all_happy(n, arrangement):
    return arrangement == ((1 << n) - 1)

   
def solution(in_file):
    """Uses the data in in_file to generate an answer as a single string to be written to file"""
    out_list = []
    
    test_cases = int(in_file.readline().strip())

    for i in range(test_cases):
        S, K = in_file.readline().strip().split()
        pancake_number = len(S)
        spatula_width = int(K)
        
        arrangement = 0
        for pancake_pos in range(pancake_number):
            face = S[pancake_pos]
            if face == '+':
                arrangement |= 1 << (pancake_number - pancake_pos) - 1
        
        if are_all_happy(pancake_number, arrangement):
            min_flip_count = 0
        else:
            min_flip_count = -1
            flip_effect = (2 ** spatula_width) - 1
            
            flip_count = 0
            for j in range(pancake_number - spatula_width + 1):
                if not(arrangement & (1 << j)):
                    arrangement ^= flip_effect
                    flip_count += 1
                
                flip_effect <<= 1
                
                if are_all_happy(pancake_number, arrangement):
                    min_flip_count = flip_count
                    break
             
        if min_flip_count >= 0:
            out_line = "Case #%d: %d" %(i+1, min_flip_count)
        else:
            out_line = "Case #%d: IMPOSSIBLE" %(i+1)
            
        out_list.append(out_line)
    
    return out_list
    

def main():
    """Opens the input file, collects the generated answer and writes it to the output file."""
    input_name = 'A-large.in'
    output_name = 'A\'s-output.txt'
    
    in_file = open(input_name)
    out_file = open(output_name, 'w')

    out_list = solution(in_file)
    out_string = '\n'.join(out_list)
    out_file.write(out_string)
    
    in_file.close()
    out_file.close()

    
if __name__ == "__main__":
    main()
    

