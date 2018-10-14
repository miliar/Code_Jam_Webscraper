import math

f = open('A-small-attempt0.in', 'r')

# read first line, number of trials
trials = int(f.readline())
for i in range(trials):
    row1 = int(f.readline())
    matrix = [[int(x) for x in f.readline().strip().split()] for j in range(0,4)]
    line1 = matrix[row1 - 1]
    row2 = int(f.readline())
    matrix = [[int(x) for x in f.readline().strip().split()] for j in range(0,4)]
    line2 = matrix[row2 - 1]
    num = [j for j in line1 if j in line2]
    print("Case #" + str(i + 1) + ':'),
    if len(num) == 0:
        print "Volunteer cheated!"
    elif len(num) == 1:
        print num[0]
    elif len(num) > 1:
        print "Bad magician!"