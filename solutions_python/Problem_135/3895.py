from sets import Set
import sys

globalcount = 1

class Input:
    def __init__(self, choice1, choice2, matrix1, matrix2):
        self.choice1 = choice1
        self.choice2 = choice2
        self.matrix1 = [tuple(row) for row in matrix1]
        self.matrix2 = [tuple(row) for row in matrix2]

    def getresult(self):
        possibilities1 = Set()
        for x in self.matrix1[self.choice1 - 1]:
            possibilities1.add(x)
        possibilities2 = Set()
        for x in self.matrix2[self.choice2 - 1]:
            possibilities2.add(x)
        possibilities = possibilities1.intersection(possibilities2)
        if len(possibilities) == 0:
            return 'Volunteer cheated!'
        elif len(possibilities) > 1:
            return 'Bad magician!'
        else:
            return possibilities.pop()

    def __unicode__(self):
        return u'(%s|%s|%s|%s)' % (self.choice1, self.choice2, self.matrix1, self.matrix2)

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()


def get_inputs(filename):
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            lines.append(line)

        inputlist = []
        i = 1
        while i < int(lines[0])*10:
            inputline = lines[i]
            choice1 = int(inputline[:-1])
            inputline = lines[i+5]
            choice2 = int(inputline[:-1])
            matrix1 = []
            j = 1
            while j < 5:
                inputline = lines[i+j]
                inputline = inputline[:-1]
                row = [int(x) for x in inputline.split(' ')]
                matrix1.append(row)
                j += 1
            matrix2 = []
            j = 6
            while j < 10:
                inputline = lines[i+j]
                inputline = inputline[:-1]
                row = [int(x) for x in inputline.split(' ')]
                matrix2.append(row)
                j += 1
            inputlist.append(Input(choice1, choice2, matrix1, matrix2))
            i += 10
        return inputlist


inputs = get_inputs(sys.argv[1])
for input in inputs:
    print(('Case #%s: ' % globalcount) + str(input.getresult()))
    globalcount += 1