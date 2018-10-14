"""
Jonathan Simowitz

Google Code Jam 2011
C - Candy Splitting
"""

import os

"""
Funciton responsible for applying the algorithm
on the test data and returning the output

I just did not see this last night.  Realized how
simple this was in my dreams last night... haha.
"""
def process(num_candy, candy_values):
    candy_values = candy_values.split(" ")
    xor_total = 0
    total = 0
    min_val = -1
    for i in range(int(num_candy)):
        candy_values[i] = int(candy_values[i])
        xor_total ^= candy_values[i]
        total += candy_values[i]

        if (min_val == -1):
            min_val = candy_values[i]
        elif (candy_values[i] < min_val):
            min_val = candy_values[i]

    if (xor_total != 0):
        return 'NO'
    else:
        return str(total - min_val)

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "C-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    Heading = True
    test_case = 1

    #Iterate through the input file
    while True:
        #read input one line at a time
        line = rf.readline()
        line = line.strip()

        if not line:
            #end of file

            #close input file
            rf.close()
            #close output file
            wf.close()
            break
        else:
            #process the line
            if (Heading):
                NUM_TEST_CASES = int(line)
                Heading = False
            else:
                line2 = rf.readline()
                line2 = line2.strip()
            
                wf.write("Case #" + str(test_case) + ": " + process(line,line2) + "\n")
                test_case += 1
            
main()
