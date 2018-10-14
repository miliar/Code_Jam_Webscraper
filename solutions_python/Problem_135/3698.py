__author__ = 'khayong'

import sys

class Case():
    def __init__(self, ans1, ans2, cards1, cards2):
        self.ans1 = ans1
        self.ans2 = ans2
        self.cards1 = cards1
        self.cards2 = cards2

    def __str__(self):
        attrs = vars(self)
        return ', '.join("%s: %s" % item for item in attrs.items())

    @staticmethod
    def get_case(file):
        ans1 = int(file.readline().strip())
        cards1 = []
        for i in range(4):
            cards1.append(file.readline().strip().split(' '))

        ans2 = int(file.readline().strip())
        cards2 = []
        for i in range(4):
            cards2.append(file.readline().strip().split(' '))

        return Case(ans1, ans2, cards1, cards2)

class Solver():
    def __init__(self, t, case):
        self.t = t
        self.case = case

    def solve(self):
        case = self.case

        row1 = case.cards1[case.ans1 - 1]
        row2 = case.cards2[case.ans2 - 1]

        result = list(set(row1).intersection(set(row2)))
        if len(result) == 1:
            print "Case #%s: %d" % (self.t, int(result[0]))
        elif len(result) > 1:
            print "Case #%s: Bad magician!" % (self.t)
        elif len(result) == 0:
            print "Case #%s: Volunteer cheated!" % (self.t)

    @staticmethod
    def solve_case(t, case):
        Solver(t, case).solve()

if __name__ == "__main__":

    cases = []

    if len(sys.argv) < 2:
        print("Please supply an input data file")
        exit()

    filename = sys.argv[1]
    file = open(filename, 'r')

    T = int(file.readline().strip())
    for t in range(T):
        case = Case.get_case(file)
        Solver.solve_case((t+1), case)