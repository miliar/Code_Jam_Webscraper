'''
This script would have template for reading and writing files for the google code jam thing.

@author: nanda
'''

##############################################################################
# This part would contain the logic for solving actual puzzle.
def solve_puzzle(input):
    input =  input.split(" ")
    res = pat_math(int(input[0]), int(input[1].strip()))
    for no in input[2:]:
        res = pat_math(int(res), int(no.strip())) 
    
    if res != 0:
        return "NO" 
    else:
        return sum(sorted(map(lambda x: int(x), input))[1:])

def pat_math(a, b):
    a = bin(a)[2:][::-1]
    b = bin(b)[2:][::-1]

    ans = []
    if len(b) > len(a):
        tmp = a
        a = b
        b = tmp
    
    for index, b_ch in enumerate(b):
        a_ch = a[index] 
        if a_ch == "1" and b_ch == "1":
            ans.append('0')
        elif a_ch == "1" or b_ch == "1":
            ans.append('1')
        else:
            ans.append('0')
    
    ans = ''.join(ans)
    ans = ans + a[len(b):]

    return int(ans[::-1], 2)
  
##############################################################################
def main():
    # Code for Reading and writing.
    # Small Files.
    #in_file_name = "C-small-practice.in"
    #out_file_name = "C-small-practice.out"
    
    # Large Files. 
    in_file_name = "C-large-practice.in"
    out_file_name = "C-large-practice.out"
    
    in_file =  "d:\codejam\problems\\" + in_file_name
    out_file = "d:\codejam\problems\\" + out_file_name
    
    reader = open(in_file)
    writer = open(out_file, 'w')
    
    reader.readline()
    for case_no, input in enumerate(reader):
        if case_no % 2 != 0:
            result = solve_puzzle(input)
            writer.write("Case #" + str(int((case_no+1)/2))+ ": " + str(result) + "\n")     
    writer.close()
    
##############################################################################
if __name__== "__main__":
    main()