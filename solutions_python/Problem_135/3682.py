import sys

file = sys.argv[1]
f = open(file, 'r')
out = open("output.txt", 'w')

numTests = int(f.readline())
for testNum in xrange(1, numTests + 1):
    row1 = int(f.readline())
    arr1 = []
    for row in range(4):
        temp = [int(i) for i in f.readline().split()]
        if row == row1-1:
            arr1 = temp
    row2 = int(f.readline())
    arr2 = []
    for row in range(4):
        temp = [int(i) for i in f.readline().split()]
        if row == row2-1:
            arr2 = temp
    #print "first " + str(row1)
    #print arr1
    #print "second" + str(row2)
    #print arr2
    res = list(set(arr1) & set(arr2))
    if len(res) < 1:
        out.write("Case #" + str(testNum) + ": Volunteer cheated!\n")
    elif len(res) == 1:
        out.write("Case #" + str(testNum) + ": " + str(res[0]) + "\n")
    else:
        out.write("Case #" + str(testNum) + ": Bad magician!\n")
