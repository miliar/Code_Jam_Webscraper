"""
Jonathan Simowitz

Google Code Jam 2012
Qualification Round
"""

import os

"""
This object contains...
"""
class dance():
    def __init__(self, total, p):
        self.total = int(total)
        self.scores = []
        for i in range(3):
            self.scores.append(self.total/3)
        i = 0
        while sum(self.scores) < self.total:
            self.scores[i] += 1
            i += 1
        self.has_p = max(self.scores) >= p
        scores = self.scores[:]
        if i == 0 and scores[0] != 10 and scores[0] != 0:
            scores[0] -= 1
            scores[1] += 1
            self.has_p_surprise = max(scores) >= p
        elif i == 1 and scores[1] != 0:
            scores[1] -= 1
            scores[2] += 1
            self.has_p_surprise = max(scores) >= p
        elif i == 2 and scores[0] != 10 and scores[2] != 0:
            scores[0] += 1
            scores[2] -= 1
            self.has_p_surprise = max(scores) >= p
        else:
            self.has_p_surprise = self.has_p

    def __str__(self):
        return str(self.total) + u' - ' + str(self.scores)

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data):
    data = data.split()
    N = int(data[0]) # Number of Googlers
    S = int(data[1]) # Number of surprising triplets
    p = int(data[2]) # Best result target
    total_scores = data[3:]
    out = 0
    for total_score in total_scores:
        score = dance(int(total_score), p)
        if score.has_p:
            out += 1
        elif S > 0 and score.has_p_surprise:
            S -= 1
            out += 1
    
    return str(out)

"""
Main function initializes files, iterates through
data, writes output, and closes the files.
"""
def main():
    #Open the input file
    rf = open(os.path.join(os.getcwd(), "B-small-attempt0.in"), "r")
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
