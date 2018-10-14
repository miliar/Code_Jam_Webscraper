#!/usr/bin/python

CASE_LENGTH = 10

class Case:
    def __init__(self, data, index):
        self.index = index

        firstGrid = [[int(s) for s in data[i].split(' ')] for i in range(1, 5)]
        secondGrid = [[int(s) for s in data[i].split(' ')] for i in range(6, 10)]

        # Retrieve the two rows named by the volunteer.
        self.row1 = firstGrid[int(data[0]) - 1]
        self.row2 = secondGrid[int(data[5]) - 1]

    def getAnswers(self):
        # Check for answers by retrieving the intersection of the two rows.
        intersection = set(self.row1).intersection(self.row2)

        msg = "Case #{}: ".format(self.index)

        if len(intersection) == 0:
            return msg + "Volunteer cheated!"
        elif len(intersection) == 1:
            return msg + str(intersection.pop())
        else:
            return msg + "Bad magician!"

def splitCases(cases, n):
    if n < 1:
        n = 1
    return [cases[i:i + n] for i in range(0, len(cases), n)]


import sys

# Read the input from stdin.
data = sys.stdin.readlines()

# Split the input into the number of cases and the cases themselves.
T, cases = int(data[0]), data[1:]
cases = splitCases(cases, CASE_LENGTH)

# Process the cases, retrieve the answers, and print them.
for i in range(0, T):
    print(Case(cases[i], i + 1).getAnswers())
