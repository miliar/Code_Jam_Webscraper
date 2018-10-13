'''
BOT TRUST.

@author: nanda
'''

##############################################################################
# This part would contain the logic for solving actual puzzle.
def solve_puzzle(input):
    input = input[2:].split(' ')
    o = []
    b = []
    for i, char in enumerate(input):
        if char in ['O', 'B']:
            if char == 'O':
                o.append(int(input[i+1].strip()))
            if char == 'B':
                b.append(int(input[i+1].strip()))

    c_o = 1
    c_b = 1
    t_l_o = 0
    t_l_b = 0
    tt = 0
    for i, char in enumerate(input):
        if char in ['O', 'B']:
            if char == 'O':
                x = int(input[i+1].strip())
                diff = abs(x-c_o)
                time_to_add = diff - t_l_o
                if time_to_add <= 0:
                    time_to_add = 0
                time_to_add += 1
                tt = tt + time_to_add
                c_o = x
                t_l_o = 0
                t_l_b = t_l_b + time_to_add
            if char == 'B':
                x =int(input[i+1].strip())
                diff = abs(x-c_b)
                time_to_add = diff - t_l_b
                if time_to_add <= 0:
                    time_to_add = 0
                time_to_add += 1
                tt = tt + time_to_add
                c_b = x
                t_l_b = 0
                t_l_o = t_l_o + time_to_add
    
    print tt
    return tt
##############################################################################
def main():
    # Code for Reading and writing.
    # Small Files.
    #in_file_name = "A-small-practice.in"
    #out_file_name = "A-small-practice.out"
    
    # Large Files. 
    in_file_name = "A-large-practice.in"
    out_file_name = "A-large-practice.out"
    
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