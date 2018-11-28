def solve(first,second, third, fourth):
    
    first = list(first[:-1])    # split each character to a list
    second = list(second[:-1])  # split each character to a list
    third = list(third[:-1])    # split each character to a list
    forth = list(fourth[:-1])    # split each character to a list

    table = [[]for i in range(4)]
    table[0] = first
    table[1] = second
    table[2] = third
    table[3] = fourth

    if  (((table[0][0] in ('X','T') and table[0][1] in ('X','T') and table[0][2] in ('X','T') and table[0][3] in ('X','T')) or
         (table[1][0] in ('X','T') and table[1][1] in ('X','T') and table[1][2] in ('X','T') and table[1][3] in ('X','T')) or
         (table[2][0] in ('X','T') and table[2][1] in ('X','T') and table[2][2] in ('X','T') and table[2][3] in ('X','T')) or
         (table[3][0] in ('X','T') and table[3][1] in ('X','T') and table[3][2] in ('X','T') and table[3][3] in ('X','T'))) or
         ((table[0][0] in ('X','T') and table[1][0] in ('X','T') and table[2][0] in ('X','T') and table[3][0] in ('X','T')) or
         (table[0][1] in ('X','T') and table[1][1] in ('X','T') and table[2][1] in ('X','T') and table[3][1] in ('X','T')) or
         (table[0][2] in ('X','T') and table[1][2] in ('X','T') and table[2][2] in ('X','T') and table[3][2] in ('X','T')) or
         (table[0][3] in ('X','T') and table[1][3] in ('X','T') and table[2][3] in ('X','T') and table[3][3] in ('X','T'))) or
         ((table[0][0] in ('X','T') and table[1][1] in ('X','T') and table[2][2] in ('X','T') and table[3][3] in ('X','T')) or
         (table[0][3] in ('X','T') and table[1][2] in ('X','T') and table[2][1] in ('X','T') and table[3][0] in ('X','T')))):
             return "X won"
    elif (((table[0][0] in ('O','T') and table[0][1] in ('O','T') and table[0][2] in ('O','T') and table[0][3] in ('O','T')) or
         (table[1][0] in ('O','T') and table[1][1] in ('O','T') and table[1][2] in ('O','T') and table[1][3] in ('O','T')) or
         (table[2][0] in ('O','T') and table[2][1] in ('O','T') and table[2][2] in ('O','T') and table[2][3] in ('O','T')) or
         (table[3][0] in ('O','T') and table[3][1] in ('O','T') and table[3][2] in ('O','T') and table[3][3] in ('O','T'))) or
         ((table[0][0] in ('O','T') and table[1][0] in ('O','T') and table[2][0] in ('O','T') and table[3][0] in ('O','T')) or
         (table[0][1] in ('O','T') and table[1][1] in ('O','T') and table[2][1] in ('O','T') and table[3][1] in ('O','T')) or
         (table[0][2] in ('O','T') and table[1][2] in ('O','T') and table[2][2] in ('O','T') and table[3][2] in ('O','T')) or
         (table[0][3] in ('O','T') and table[1][3] in ('O','T') and table[2][3] in ('O','T') and table[3][3] in ('O','T'))) or
         ((table[0][0] in ('O','T') and table[1][1] in ('O','T') and table[2][2] in ('O','T') and table[3][3] in ('O','T')) or
         (table[0][3] in ('O','T') and table[1][2] in ('O','T') and table[2][1] in ('O','T') and table[3][0] in ('O','T')))):
            return "O won"
    elif any('.' in i for i in table):
             return "Game has not completed"
    else:
            return "Draw"
    return "none"

infile = open('A-large.in','r') # open input file
output_file = open("output.txt", "w") # open output file

t = int(infile.readline())  # read number of test case

testcase = 1

for first in infile: # start from the second line
    second = infile.next()
    third = infile.next()
    fourth = infile.next()
    empty = infile.next()
    
    output_file.write("Case #" + str(testcase) + ": " + str(solve(first,second,
                                                third, fourth))+"\n")
    testcase+=1

infile.close() # close input file
output_file.close() # close output file

