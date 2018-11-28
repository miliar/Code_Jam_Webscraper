def ReadSingleMatrix(inp):
    row = []
    answer = int(inp.readline())
    for rowNumber in range(1, 5):
        if answer == rowNumber:
            row = inp.readline().rstrip().split(' ')
        else:
            inp.readline() # discard useless row
    return row

def OutputSingleCase(x, y):
    if len(y) == 0:
        y = "Volunteer cheated!"
    elif len(y) > 1:
        y = "Bad magician!"
    else:
        y = y[0]

    print "Case #" + str(x) + ": " + str(y)

inp = file('input.txt', 'r')

numberOfCases = int(inp.readline())

for case in range(1, numberOfCases+1):
    row1 = ReadSingleMatrix(inp)
    row2 = ReadSingleMatrix(inp)
    OutputSingleCase(case, [val for val in row1 if val in row2])
