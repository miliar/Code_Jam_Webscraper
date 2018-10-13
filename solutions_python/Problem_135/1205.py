#!/usr/bin/python
import sys, getopt

__author__ = 'cdriscoll'


class Trick:
    testNum = 0
    ans1 = 0
    ans2 = 0
    rows1 = [[]]
    rows2 = [[]]

    def __init__(self, testNum, ans1, ans2, rows1, rows2):
        self.testNum = testNum
        self.ans1 = ans1
        self.ans2 = ans2
        self.rows1 = rows1
        self.rows2 = rows2

    def solve(self):
        numCorrect = 0
        correctElem = 0
        for elem in self.rows1[self.ans1 - 1]:
            if elem in self.rows2[self.ans2 - 1]:
                numCorrect += 1
                correctElem = elem

        if numCorrect == 0:
            return "Case #%d: Volunteer cheated!\n" % self.testNum
        elif numCorrect == 1:
            return "Case #%d: %d\n" % (self.testNum, correctElem)
        elif numCorrect > 1:
            return "Case #%d: Bad magician!\n" % self.testNum


def main(argv):
    infile = ''
    outfile = ''


    try:
        opts, args = getopt.getopt(argv, "i:o:", ["ifile=", "ofile"])
    except getopt.GetoptError:
        print 'magic.py -i <inputfile> -o <outputfile'
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i", "--ifile"):
            infile = arg
        elif opt in ("-o", "--ofile"):
            outfile = arg

    fd_in = open(infile, 'r')
    fd_out = open(outfile, 'a')

    numTests = int(fd_in.readline())

    for i in range(1, numTests + 1):
        rows1 = []
        rows2 = []
        ans1 = int(fd_in.readline())
        for j in range(0, 4):
            rows1.append(map(int, fd_in.readline().split(' ')))
        ans2 = int(fd_in.readline())
        for j in range(0, 4):
            rows2.append(map(int, fd_in.readline().split(' ')))

        test = Trick(i, ans1, ans2, rows1, rows2)
        fd_out.write(test.solve())




if __name__ == '__main__':
    main(sys.argv[1:])
