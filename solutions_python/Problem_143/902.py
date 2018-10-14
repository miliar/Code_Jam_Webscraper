__author__ = 'wojnar'

import sys

class ri:

    def run(self):
        input = sys.argv[1]
        #output = 'wojnar_output.txt'

        with open(input, 'r') as infile:#, open(output, 'w')as outfile:
            numberOfTestCases = infile.readline()

            for i in xrange(0, int(numberOfTestCases)):
                row = infile.readline()
                new_row =  row.split(' ')
                A = new_row[0].strip()
                B = new_row[1].strip()
                K = new_row[2].strip()
                result = self.solve(int(A), int(B), int(K) )
                self.outputResult(i, result)

    def outputResult(self, i, result):
        print 'Case #%i: %s' % (i+1, result)



    def solve(self, A, B, K):
        n = 0
        for a in xrange(0, A):
            for b in xrange(0, B):
                if a & b  < K:
                    n +=1
        return n



if __name__ == "__main__":

    m = ri()

    m.run()