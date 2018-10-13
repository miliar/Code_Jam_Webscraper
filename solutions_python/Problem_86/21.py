"""
Jonathan Simowitz

Google Code Jam 2011
Round 1C Question 3
Perfect Harmony
"""

import os

"""
This object contains...
"""
class object():
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data, rf):
    data = data.split(" ")
    N = int(data[0])
    L = int(data[1])
    H = int(data[2])

    data = rf.readline()
    data = data.strip()
    data = data.split(" ")
    notes = []
    for item in data:
        value = int(item)
        notes.append(value)

    for i in range(L,H+1):
        goodNote = True
        for value in notes:
            if (value%i != 0) and (i%value != 0):
                goodNote = False
                break
        if (goodNote):
            return str(i)
            
    return 'NO'

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "C-small-attempt0.in"), "r")
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
                wf.write("Case #" + str(test_num) + ": " + process(line, rf) + "\n")
                #increment the test case number
                test_num += 1

main()
