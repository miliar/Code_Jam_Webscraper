#inputFile = open('test.txt', 'r')
inputFile = open('D-small-attempt6.in', 'r')
#inputFile = open('A-large.in.txt', 'r')


# keep track of number of cases
num_case = int(inputFile.readline())

for case in range(1, num_case+1):
    line = inputFile.readline()
    value_strings = line.split()
    X = int(value_strings[0])
    R = int(value_strings[1])
    C = int(value_strings[2])

    blocks = R * C
    if (blocks % X != 0):
        output = 'RICHARD'
    else:
        if (R == 1 or C == 1) and X > 2:
            output = 'RICHARD'
        elif (R * C == X) and X > 2:
            output = 'RICHARD'
        elif X == 4:
            if (R * C == 8):
                output = 'RICHARD'
            else:
                output = 'GABRIEL'
        else:
            output = 'GABRIEL'

    print 'Case #' + str(case) + ': ' + output
