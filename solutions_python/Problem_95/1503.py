"""
Jonathan Simowitz

Google Code Jam 2012
Qualification Round
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

sample = {'ejp mysljylc kd kxveddknmc re jsicpdrysi': 'our language is impossible to understand',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd': 'there are twenty six factorial possibilities',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv': 'so it is okay if you want to just give up'}

decoder = {'y': 'a',
           'e': 'o',
           'q': 'z'}

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data):
    ret = ''
    for i in range(len(data)):
        ret = ret + decoder[data[i]]
    return ret

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "A-small-attempt0.in"), "r")
    #Open the output file
    wf = open(os.path.join(os.getcwd(), "output.txt"), "w")

    heading = True
    test_num = 1

    for k,v in sample.iteritems():
        for i in range(len(k)):
            decoder[k[i]] = v[i]
    decoder['z'] = 'q'

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
