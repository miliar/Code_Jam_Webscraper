__author__ = 'jbojcic'

def main():
    f = open('A-small-attempt1.in', 'r')
    f2 = open('A-small-attempt1-output.in', 'w')
    numOfTestCases = f.readline()

    for i in range(int(numOfTestCases)):
        guess1 = int(f.readline())
        matrix1 = []
        for j in range(4):
            line = f.readline()
            line = line[0:-1].split(' ')
            rowNumbers = list(map(int, line))
            matrix1.append(rowNumbers)
        guess2 = int(f.readline())
        matrix2 = []
        for k in range(4):
            line = f.readline()
            line = line[0:-1].split(' ')
            rowNumbers = list(map(int, line))
            matrix2.append(rowNumbers)
        row1 = matrix1[guess1-1]
        row2 = matrix2[guess2-1]
        intersection = list(set(row1) & set(row2))
        if len(intersection) == 0:
            f2.write("Case #" + str(i+1) + ": Volunteer cheated!\n")
        elif len(intersection) == 1:
            f2.write("Case #" + str(i+1) + ": " + str(intersection[0]) + "\n")
        else:
            f2.write("Case #" + str(i+1) + ": Bad magician!\n")
    f.close()

main()

