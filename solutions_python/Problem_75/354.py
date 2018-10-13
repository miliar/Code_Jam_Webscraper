'''

Magika.

@author: nanda
'''

##############################################################################
# This part would contain the logic for solving actual puzzle.
def solve_puzzle(input):
    replacers = {}
    clearers = {}
    result = []
    
    input = input.split(' ')
    index = 0
    
    replacer_count = int(input[index])
    index = index + 1
    
    replacer_strings = input[index: index+replacer_count]
    for string in replacer_strings:
        if not replacers.has_key(string[0]):
            replacers[string[0]] = {}         
        replacers[string[0]][string[1]] = string[2]
        
        if not replacers.has_key(string[1]):
            replacers[string[1]] = {}  
        replacers[string[1]][string[0]] = string[2]
    
    index = index + replacer_count 
    
    clearer_count = int(input[index])
    index = index + 1
    
    clearer_strings = input[index: index + clearer_count] 
    for string in clearer_strings:
        if not clearers.has_key(string[0]):
            clearers[string[0]] = []
        clearers[string[0]].append(string[1])
        
        if not clearers.has_key(string[1]):
            clearers[string[1]] = []
        clearers[string[1]].append(string[0])
    
    index = index + clearer_count   
        
    input_string = input[index: ][1].strip()
    
#    print input_string
#    print replacers
#    print clearers
#    
    # Main logic starts here.
    for char in input_string:
        flag = 0
        if char in replacers.keys():
            replacer_bros = replacers[char]
            if len(result) > 0:
                if result[-1] in replacer_bros.keys():
                    result[-1] = replacer_bros[result[-1]]
                    char = result[-1]
                    flag = 1       
        if char in clearers.keys():
            clearer_bros = clearers[char]
            if len(list(set(clearer_bros).intersection(set(result)))) > 0:
                result = []
                continue
        if flag == 0:
            result.append(char)
    
    result_string = "["
    for res in result:
        result_string = result_string + res
        result_string = result_string + ', '
    if result:
        result_string = result_string[:-2]
    return result_string + "]"
##############################################################################
def main():
    # Code for Reading and writing.
    # Small Files.
    #in_file_name = "B-small-practice.in"
    #out_file_name = "B-small-practice.out"
    
    # Large Files. 
    in_file_name = "B-large-practice.in"
    out_file_name = "B-large-practice.out"
    
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')
    
    reader.readline()
    for case_no, input in enumerate(reader):
        result = solve_puzzle(input)
        writer.write("Case #" + str(case_no+1)+ ": " + str(result) + "\n")   
    writer.close()
    
##############################################################################
if __name__== "__main__":
    main()