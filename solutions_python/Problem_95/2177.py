"""this program reads all ".in" files in current directory and parses them for google code jam. 
then iterates trough each test case in each file and applies the solution.
after the files are solved it will write the results in google code jam format to the same
name ".out" files"""

import os

class CodeJam():
    def __init__(self, solutionCallback):
        self.solutionCallback = solutionCallback
        self.testFiles = [];
        self.readInputFiles()
        self.solve()
        self.writeResults()
        print("Done!")
         
    def readInputFiles(self):
        directoryContents = os.listdir('.')
        for fileName in directoryContents:
            if(self.isInputFile(fileName)):
                self.readFile(fileName)

    def isInputFile(self, fileName):
        return (os.path.splitext(fileName)[1] == '.in')          
            
    def readFile(self, fileName):
        file = open(fileName)
        fileContents = file.readlines()
        file.close();
        testsInFile = int(fileContents.pop(0))
        linesInTest = int(len(fileContents)/testsInFile)
        tests = []
        while len(fileContents) > 0 :
            tests.append(self.readTest(fileContents, linesInTest))
        self.testFiles.append({'fileName':fileName, 'tests':tests})

    def readTest(self, fileContents, linesInTest):
        test = []
        for line in range(linesInTest):
            test.append(fileContents.pop(0))
        return test

    def solve(self):
        for file in self.testFiles:
            self.solveFile(file)

    def solveFile(self, file):
        solutions = []
        for test in file["tests"]:
            solutions.append(self.solutionCallback(test))
        file["solutions"]  = solutions

    def writeResults(self):
        for file in self.testFiles:
            self.writeResultsFile(file)

    def writeResultsFile(self, file):
        resultsFile = open(os.path.splitext(file["fileName"])[0] + ".out", "w+")
        counter = 1
        for solution in file["solutions"]:
            resultsFile.write("Case #" + str(counter)  + ": " + solution + "\n")
            counter += 1
        resultsFile.close()
	
def solution(testCase):
	"""check q and z"""
	dictionary = {'y': 'a', 'n': 'b', 'f': 'c', 'i': 'd', 'c': 'e', 'w' : 'f', 'l': 'g', 'b': 'h', 'k': 'i', 'u': 'j', 'o': 'k', 'm': 'l', 'x': 'm', 's': 'n', 'e': 'o', 'v': 'p', 'z':'q', 'p': 'r', 'd': 's', 'r': 't', 'j': 'u', 'g': 'v', 't': 'w', 'h': 'x', 'a': 'y', 'q': 'z', ' ': ' '}
	result = ""
	testCase = testCase[0].rstrip('\r\n')
	for char in testCase:
		result += dictionary[char]
	return str(result)

if __name__ == "__main__":
    jam =  CodeJam(solution)
