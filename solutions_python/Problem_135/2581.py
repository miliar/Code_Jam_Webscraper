#!/usr/bin/python


def solveProblem(fw, iteration, row1, row2):
    number = ""
    line1 = row1.split()
    line2 = row2.split()
    intersect = list(set(line1) & set(line2))
    if (len(intersect) == 1):
        fw.write("Case #"+str(iteration)+": "+str(intersect[0])+"\n")
    elif (len(intersect) > 1):
        fw.write("Case #"+str(iteration)+": Bad magician!\n")
    else:
        fw.write("Case #"+str(iteration)+": Volunteer cheated!\n")

def readProblemData():
    fr = open('A-small-attempt5.in', 'r')
    lines = fr.readlines()
    fw = open('results_magic_trick.txt', 'w')
    num_cases = int(lines[0])
    j = 1
    for i in range(1, num_cases + 1):
        first_row = int(lines[j])
        row1 = lines[j+first_row]
        second_row = int(lines[j+5])
        row2 = lines[j+5+second_row]
        solveProblem(fw, i, row1, row2)
        j += 10
    fr.close()
    fw.close()


if __name__ == "__main__":
    readProblemData()
