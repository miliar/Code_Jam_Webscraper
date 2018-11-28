#!/usr/bin/python

#checks if n and m are recycled, as per challenge description
def is_recycled(n,m):
    n = str(n)
    m = str(m)
    if len(n) != len(m):
        return False
    if n == m:
        return True
    for i in range(len(n)-1):
        n = n[-1] + n[:-1]
        if n == m:
            return True
    return False

#open the input file and read it
input_file = open('C-small-attempt0.in','r')
input_lines = input_file.readlines()
input_file.close()
#get the number of cases
number_of_cases = int(input_lines.pop(0))
#initialize the output string
output = ""

for i in range(1, number_of_cases+1):
    strings = input_lines.pop(0).split(' ')
    A = strings[0]
    B = strings[1]
    A = int(A)
    B = int(B)
    #count how man recycled numbers there are
    recycled_numbers = 0
    #for each possible n
    for n in range(A,B):
        #and each possible m given n
        for m in range(n+1,B+1):
            #check if recycled
            if is_recycled(n,m):
                #if so, record it
                recycled_numbers += 1
    #finally, add results to output string
    output = output +  'Case #' + str(i) + ': ' + str(recycled_numbers) + '\n'

#finally, write to output file
output_file = open('output','w')
output_file.write(output)
output_file.close()
