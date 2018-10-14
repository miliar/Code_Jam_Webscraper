"""
Jonathan Simowitz

Google Code Jam 2011
"""

import os

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data_len, data):
    data_len = int(data_len)
    data = data.split(" ")

    items = []
    for item in data:
        items.append(int(item))

    sorted_items = list(items)
    sorted_items.sort()

    count = 0
    for i in range(len(items)):
        if (items[i] != sorted_items[i]):
            count += 1
            
    return str(count) + ".000000"

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "D-large.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    Heading = True
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
            if (Heading):
                Heading = False
                NUM_TEST_CASES = int(line)
            else:
                line2 = rf.readline()
                line2 = line2.strip()
                
                wf.write("Case #" + str(test_num) + ": " + process(line,line2) + "\n")
                test_num += 1
            
main()
