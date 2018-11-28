"""
Jonathan Simowitz

Google Code Jam 2011
Round 1B Question 1
RPI
"""

import os

"""
Funciton responsible for applying the algorithm
on the test data and returning the output
"""
def process(data, rf):
    num_teams = int(data)

    data = []
    for i in range(num_teams):
        line = rf.readline()
        data.append(line)

    #calculate WP for each team
    WPs = []
    for i in range(num_teams):
        wins = 0
        total = 0
        for j  in range(num_teams):
            if (data[i][j] == '0'):
                total += 1
            elif (data[i][j] == '1'):
                total += 1
                wins += 1
        #wins, totals, WP
        WPs.append((float(wins), float(total), float(wins)/float(total)))

    #calculate OWP for each team
    OWPs = []
    for i in range(num_teams):
        total = 0.0
        num_opponents = 0
        for j in range(num_teams):
            if (data[i][j] == '0'):
                total += ((WPs[j][0]-1.0) / (WPs[j][1]-1.0))
                num_opponents += 1
            elif (data[i][j] == '1'):
                total += ((WPs[j][0]) / (WPs[j][1]-1.0))
                num_opponents += 1
        OWPs.append((total, num_opponents, total/float(num_opponents)))

    #calculate the OOWP for each team
    OOWPs = []
    for i in range(num_teams):
        total = 0.0
        num_opponents = 0
        for j in range(num_teams):
            if (data[i][j] != '.'):
                total += OWPs[j][2]
                num_opponents += 1

        OOWPs.append(total/float(num_opponents))

    output = "\n"
    for i in range(num_teams):
        value = (0.25 * WPs[i][2]) + (0.5 * OWPs[i][2]) + (0.25 * OOWPs[i])
        output += str(value) + "\n"

    return output

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
                wf.write("Case #" + str(test_num) + ":" + process(line, rf))
                #increment the test case number
                test_num += 1

main()
