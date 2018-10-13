import numpy as np
import math

class TidyNumbers:
    def readFile(self):
        # raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
        # This is all you need for most Google Code Jam problems.
        self.cases = []
        self.numCases = 0

        self.numCases = int(raw_input())  # read a line with a single integer
        for i in xrange(1, self.numCases + 1):
            n = raw_input()
            # n = map(int, raw_input().split())  # read a list of integers, 2 in this case
            characters = [int(character) for character in n]
            self.cases.append(characters[::-1])

    def printResult(self, results):
        for i in xrange(len(results)):
            n = results[i]
            print "Case #{}: {}".format(i + 1, n)

    def run(self):
        self.readFile()
        self.results = self.process(self.cases)
        self.printResult(self.results)

    def process(self, cases):
        results = []
        for n in cases:
            results.append(self.getNumbers(n))

        return results

    # def checkTidy(self, numList):
    #     result = True
    #     for i in range(len(numList) - 1):
    #         if (numList[i] <= numList[i + 1]):
    #             result = False
    #             break
    #     return result

    def getNumbers(self, numList):
        i = 0
        while i != len(numList) - 1:
            if numList[i] < numList[i + 1]:
                # Lower digits, fill with 9
                for j in range(i + 1):
                    numList[j] = 9
                # Upper digit
                if numList[i + 1] == 1:
                    numList[i + 1] = 0
                else:
                    numList[i + 1] -= 1
            i += 1

        results = numList[::-1]
        if results[0] == 0:
            results = results[1:]

        return "".join(str(e) for e in results)



def main():
    q1 = TidyNumbers()
    q1.run()


if  __name__ =='__main__':
    main()
