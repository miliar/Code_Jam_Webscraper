"""
Jonathan Simowitz

Google Code Jam 2011
Round 1A
"""

import os

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data):
    data = data.split(" ")
    N = int(data[0]) #played N or less games today
    Pd = float(data[1]) #won Pd% of games played today
    Pg = int(data[2]) #won Pg% of games played in total

    if (Pg == 100) and (Pd < 100):
        return "Broken"
    elif (Pg == 0) and (Pd > 0):
        return "Broken"

    D = N
    while (D > 0):
        factor = Pd/(100.0/float(D))
        if (factor == int(factor)):
            #possible for today
            return "Possible"

        D -= 1

    return "Broken"
            

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "A-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    heading = True
    test_num = 1

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

            if (heading):
                heading = False
                NUM_TEST_CASES = int(line)
            else:
                #print the output
                wf.write("Case #" + str(test_num) + ": " + process(line) + "\n")
                #increment the test case number
                test_num += 1

main()
