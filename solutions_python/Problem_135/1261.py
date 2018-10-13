__author__ = 'st_lim'


answer1 = 0
answer2 = 0
rows1 = []
rows2 = []

import sys
myfile = open(sys.argv[1], 'r')
myoutfile = open('output.txt', 'w')
n_cases = int(myfile.readline())
for i in range(1, n_cases + 1):
    answer1 = int(myfile.readline())-1
    rows1 = []
    for j in range(0,4):
        rows1.append(myfile.readline().split())
    answer2 = int(myfile.readline())-1
    rows2 = []
    for j in range(0, 4):
        rows2.append(myfile.readline().strip())

    row1 = rows1[answer1]
    row2 = " " + rows2[answer2] + " "
    matches = []
    for card in row1:
        if row2.find(" " + card + " ") > -1:
            matches.append(card)

    result = 0
    if len(matches) == 0:
        result = "Volunteer cheated!"
    elif len(matches) > 1:
        result = "Bad magician!"
    else:
        result = matches[0]
    output = "Case #{0}: {1}\n".format(i, result)
    print output
    myoutfile.write(output)