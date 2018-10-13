__author__ = 'wojnar'

import sys

class cca:
    def run(self):
        input = sys.argv[1]

        with open(input, 'r') as infile:#, open(output, 'w')as outfile:
            numberOfTestCases = infile.readline()

            for i in xrange(0, int(numberOfTestCases)):
                row = infile.readline()
                case = row.split(' ')
                C = float(case[0].strip())
                F = float(case[1].strip())
                X = float(case[2].strip())
                result = self.solve(C, F, X)
                self.outputResult(i, round(result, 7))

    def solve(self, C, F, X):
        #deposit = 0.0
        alreadyrun = 0.0
        currentRatePerSecond = 2.0
        Xreached = False
        while not Xreached:
            currentFinishIn = self.finishedWithRate( currentRatePerSecond, X)
            (currentFinishWithNextFactory, timeToNextFactory, newRate) = self.finishWithNextFactory( currentRatePerSecond, C, F, X)
            if currentFinishWithNextFactory < currentFinishIn:
                currentRatePerSecond = newRate
                alreadyrun += timeToNextFactory
            else:
                Xreached = True
                alreadyrun += currentFinishIn
        return alreadyrun

    def finishedWithRate(self, currentrate, X):
        return X/currentrate

    def finishWithNextFactory(self, currentRate, C, F, X):
        timeToNextFactory = self.finishedWithRate(currentRate, C)
        newRate = currentRate + F
        timetofinish = self.finishedWithRate(newRate, X)
        return (timeToNextFactory+timetofinish, timeToNextFactory, newRate)



    def IsApproximatelyEqual(self, x, y, epsilon):
      """Returns True iff y is within relative or absolute 'epsilon' of x.

      By default, 'epsilon' is 1e-6.
      """
      # Check absolute precision.
      if -epsilon <= x - y <= epsilon:
        return True

      # Is x or y too close to zero?
      if -epsilon <= x <= epsilon or -epsilon <= y <= epsilon:
        return False

      # Check relative precision.
      return (-epsilon <= (x - y) / x <= epsilon
           or -epsilon <= (x - y) / y <= epsilon)

    def outputResult(self,testcase, result):
        print 'Case #%i: %s' % (testcase+1, result)



if __name__ == "__main__":

    c = cca()

    c.run()