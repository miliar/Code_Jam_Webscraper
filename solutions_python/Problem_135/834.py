import sys


class Prob1(object):
    def __init__(self, try1, board1, try2, board2):
        self.try1 = try1
        self.board1 = board1
        self.try2 = try2
        self.board2 = board2

    def solve(self):
        posibilities1 = set(self.board1[self.try1-1])
        posibilities2 = set(self.board2[self.try2-1])

        intersection = list(posibilities1 & posibilities2)

        if len(intersection) == 0:
            return "Volunteer cheated!"
        elif len(intersection) == 1:
            return str(intersection[0])
        else:
            return "Bad magician!"

output = "Case #%d: %s"

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    for counter in xrange(T):
        tries = []
        boards = []
        for k in xrange(2):
            tries.append(int(f.readline()))
            boards.append([])
            for i in xrange(4):
                line = f.readline()
                boards[k].append([int(j) for j in line.split()])
        p1 = Prob1(tries[0], boards[0], tries[1], boards[1])
        print output % (counter+1, p1.solve())
