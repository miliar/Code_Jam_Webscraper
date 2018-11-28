__author__ = 'wojnar'

import sys
import collections

class MagicTrick:

    def run(self):
        input = sys.argv[1]
        output = 'wojnar_output.txt'

        with open(input, 'r') as infile, open(output, 'w')as outfile:
            numberOfTestCases = infile.readline()

            for i in xrange(0, int(numberOfTestCases)):
                firstrow = infile.readline()
                case1 = []
                for j in xrange(0, 4):
                    line = infile.readline()
                    row = line.split(' ')
                    row[3] = row[3].strip()
                    case1.append(row)
                secondrow = infile.readline()
                case2 = []
                for j in xrange(0, 4):
                    line = infile.readline()
                    row = line.split(' ')
                    row[3] = row[3].strip()
                    case2.append(row)

                result = self.solve(firstrow, secondrow, case1, case2)
                #print firstrow
                #print case1
                #print secondrow
                #print case2
                self.outputResult(i, result)

    def outputResult(self, i, result):
        print 'Case #%i: %s' % (i+1, result)

    def solve(self, firstRow, secondRow, case1, case2):

        caseall = case1[int(firstRow)-1] + case2[int(secondRow)-1]
        length = len(caseall) - len(set(caseall))
        if length == 0:
            return 'Volunteer cheated!'
        elif length == 1:
            return str([x for x, y in collections.Counter(caseall).items() if y > 1][0])
        else:
            return 'Bad magician!'





if __name__ == "__main__":

    m = MagicTrick()

    m.run()