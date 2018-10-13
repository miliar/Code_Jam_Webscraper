'''
(c) Hannes Frank 2013
'''

class Solver():
    ''' Framework for Google CodeJam'''

    def __init__(self, task, testCaseSpec, solve, extraCasts=None):
        self.testCaseSpec = testCaseSpec
        self.solveTestCase = solve

        self.inputFileName  = '{task}.in'.format(task = task)
        self.outputFileName = '{task}.out'.format(task = task)
        self.outputPrefix   = 'Case #{testCaseNum}:'

        self.casts = {
            '#': int,           # int
            '.': float,         # float
            '$': lambda x: x    # string
        }
        self.multiLineMarker = '*'

        self.numberOfProcesses = 4

    def solve(self):
        # todo multiprocessing workaround
        # from multiprocessing import Pool
        # with open(self.inputFileName, 'r') as inputFile, open(self.outputFileName, 'w') as outputFile, Pool(processes=self.numberOfProcesses) as pool:
        #     testCases = self.processInput(inputFile, self.testCaseSpec)
        #     for i, result in enumerate(pool.map(lambda d: self.solveTestCase(**d), testCases)):
        #         print(self.outputPrefix.format(testCaseNum = i+1), result, file=outputFile)
        with open(self.inputFileName, 'r') as inputFile, open(self.outputFileName, 'w') as outputFile:
            testCases = self.processInput(inputFile, self.testCaseSpec)
            for i, result in enumerate(map(lambda d: self.solveTestCase(**d), testCases)):
                print(i+1, 'of', self.N)
                print(self.outputPrefix.format(testCaseNum = i+1), result, file=outputFile)


    def processInput(self, inputFile, testCaseSpec):
        testCaseLines = [line.strip() for line in testCaseSpec.splitlines() if line.strip()]
        print(testCaseLines)
        testCases = []

        # first line should always be the number of testcases
        self.N = int(inputFile.readline().strip())
        for i in range(self.N):
            testCase = {}

            for testCaseLine in testCaseLines:
                if testCaseLine[0] != self.multiLineMarker: # parse single line
                    line = inputFile.readline().rstrip('\n')
                    testCase.update(self.parseLine(testCaseLine, line))
                else: #parse multiline
                    s = testCaseLine[1:]
                    (timesVar, m, s) = s.partition(self.multiLineMarker)
                    times = testCase[timesVar]

                    (key, m, specLine) = s.partition(self.multiLineMarker)
                    lines = []
                    for i in range(times):
                        line = inputFile.readline().rstrip('\n')
                        lines.append(self.parseLine(specLine, line))
                    testCase[key] = lines

            testCases.append(testCase)
        return testCases


    def parseLine(self, specLine, line):
        d = {}
        # todo: values are always space separated! - Quali Africa 2010 C
        for spec in specLine.strip().split(' '):

            if spec[0] == spec[1]:
                # listmode: space separated
                # todo: parsing - list is the last of the line: assert spec is empty
                d[spec[2:]] = [self.casts[spec[0]](token) for token in line.split(' ')]
                return d
            else:
                (token, m, line) = line.partition(' ')
                d[spec[1:]] = self.casts[spec[0]](token)
        return d
# test
if __name__ == '__main__':
    def solve(n, p, lines):
        print(n, p, lines)
        return str(sum([sum(numList['nums']) for numList in lines]))

    testCaseSpec = '''
    #n #p
    *n*lines* #n1 ##nums
    '''

    Solver('test', testCaseSpec, solve).solve()