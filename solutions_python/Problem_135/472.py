#!/usr/bin/python

import sys




def process(l1, l2):
    pair = 0
    for num1 in l1.split(" "):
#        print "num1:", num1
        for num2 in l2.split(" "):
            #print num2
            if num1 == num2:
                pair += 1
                num_valid = num1
            if pair == 2:
                return "Bad magician!"
    if pair == 0:
        return "Volunteer cheated!"
    else:
        return num_valid


fin = open(sys.argv[1], 'r')

fout = open(sys.argv[1].split(".")[0] + ".out", "w")

nb_cases = int(fin.readline())

for i in range(1, nb_cases + 1):
    first_choice = int(fin.readline())
    for row in range(1, 5):
        if row == first_choice:
            line1 = fin.readline().strip()
        else:
            fin.readline()

    second_choice = int(fin.readline())
    for row in range(1, 5):
        if row == second_choice:
            line2 = fin.readline().strip()
        else:
            fin.readline()

    fout.write("Case #%d: %s\n" % (i, process(line1, line2)))

fout.flush()
fout.close()
fin.close()



# print "toto"
