'''
This script would have template for reading and writing files for the google code jam thing.

@author: nanda
'''

##############################################################################
# This part would contain the logic for solving actual puzzle.
def solve_puzzle(high, low, freq):
    x = low
    while(x != high+1):
        flag = 0
        for f in freq:
            if f%x != 0 and x%f != 0:
                flag = 1
                break
        if flag == 0:
            return x
        x = x +1
    
    return "NO"
  
##############################################################################
def main():
    # Code for Reading and writing.
    # Small Files.
    in_file_name = "C-small-attempt0.in"
    out_file_name = "C-small-attempt0.out"
    
    # Large Files. 
    #in_file_name = "A-large-practice.in"
    #out_file_name = "A-large-practice.out"
    
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')

    lines = reader.readlines()[1:]
    case_no = 0
    while(len(lines) > 0):
        x = lines[0].split(' ')

        low = int(x[1].strip())
        high = int(x[2].strip())
        lines = lines[1:]
        
        freq = lines[0]
        freq = freq.split(' ')
        freq = map(lambda x: int(x.strip()), freq)
        lines = lines[1:]
        
        result = solve_puzzle(high, low, freq)
        writer.write("Case #" + str(case_no+1)+ ": " + str(result) + "\n")   
        case_no = case_no + 1 
    writer.close()
    
##############################################################################
if __name__== "__main__":
    main()