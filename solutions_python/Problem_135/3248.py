__author__ = 'diana fisher'

filename = "A-small-attempt0.in"
inputFile = open(filename, "r")
lines = []
for line in inputFile:
    lines.append( line.strip() )

inputFile.close()

line_number = 0
numCases = int(lines[line_number])
# print 'num cases = ', numCases

line_number+=1

for i in range(numCases):
    # print '----------------------------------------------------'
    case = "Case #" + str(i+1) + ":"
    first_arrangement = []
    first_answer = (int)(lines[line_number])
    # print 'first_answer:', first_answer
    for n in range(4):
        line_number += 1
        first_arrangement.append(lines[line_number])
    line_number += 1
    # print 'first_arrangement:', first_arrangement

    second_answer = (int)(lines[line_number])
    # print 'second_answer:', second_answer
    second_arrangement = []
    for n in range(4):
        line_number += 1
        second_arrangement.append(lines[line_number])
    line_number += 1    #
    # print 'second_arrangement:', second_arrangement

    # check for matching numbers in the rows from each answer..
    first_row = first_arrangement[first_answer-1]
    second_row = second_arrangement[second_answer-1]

    cardsA = first_row.split()
    cardsB = second_row.split()
    matching = set(cardsA) & set(cardsB)

    # print 'matching:', matching
    y = None
    matching = list(matching)
    if len(matching) == 1:
        y = matching[0]
    elif len(matching) > 1:
        y = 'Bad magician!'
    else:
        y = 'Volunteer cheated!'

    print case, y











