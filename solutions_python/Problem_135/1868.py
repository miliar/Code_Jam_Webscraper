import sys

j = 1
first_row = []
second_row = []
intersect = []
of = open("/Users/nalinbhardwaj/Downloads/GCJ-2014-master/Qualification Round/Magic Trick/small_output.out", "w+")
fo = open("/Users/nalinbhardwaj/Downloads/GCJ-2014-master/Qualification Round/Magic Trick/A-small-attempt0.in", "r+")

no_of_cases = int(fo.next())

for line in fo:
    first_row_no = int(line)
    for i in range(0, first_row_no):
        first_row = fo.next().split()
    for i in range(0, 4 - first_row_no):
        fo.next()

    second_row_no = int(fo.next())
    for i in range(0, second_row_no):
        second_row = fo.next().split()
    for i in range(0, 4 - second_row_no):
        fo.next()

    intersect = list(set(first_row) & set(second_row))

    if (len(intersect) == 1):
        of.write("Case #" + str(j) + ": " + str(intersect[0] + "\n"))
    elif (len(intersect) > 1):
        of.write("Case #" + str(j) + ": Bad magician!" + "\n")
    else:
        of.write("Case #" + str(j) + ": Volunteer cheated!" + "\n")

    j += 1

of.close()
fo.close()        