from builtins import len, int
from _ast import Str

fdata = open("A-small-attempt0.in", mode = 'r')
if __name__ == "__main__":
    nbTest = int(fdata.readline())

    for n in range(nbTest):

        volunteerRow1 = int(fdata.readline())
        matrix1 = []
        matrix2 = []
        for i in range(4):
            line = fdata.readline()
            cols = line.split()
            matrix1.append(cols)

        volunteerRow2 = int(fdata.readline())
        for i in range(4):
            line = fdata.readline()
            cols = line.split()
            matrix2.append(cols)

        # print("Matrix1")
        for i in range(4):
            if i == volunteerRow1 - 1:
                # print("** {0} **".format(matrix1[i]))
                lineVolunteerMatrix1 = matrix1[i]
            else:
                pass
                # print("{0}".format(matrix1[i]))
        # print("Matrix2")
        for i in range(4):
            if i == volunteerRow2 - 1:
                # print("** {0} **".format(matrix2[i]))
                lineVolunteerMatrix2 = matrix2[i]
            else:
                pass
                # print("{0}".format(matrix2[i]))

        theMagicHappen = [number for number in lineVolunteerMatrix1 if number in lineVolunteerMatrix2]
        if len(theMagicHappen) == 1:
            print("Case #{0}: {1}".format(n + 1, theMagicHappen[0]))
        elif len(theMagicHappen) > 1:
            print("Case #{0}: Bad magician!".format(n + 1))
        elif len(theMagicHappen) == 0:
            print("Case #{0}: Volunteer cheated!".format(n + 1))
