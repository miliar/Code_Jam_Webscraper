#!/usr/bin/env python

__author__ = 'pal-andreich'


class TestCase:
    def __init__(self, numCases):
        self.numCases = numCases
        self.cases = {}
        self.__currentCase = 0

    def addTestCase(self, **kwargs):
        self.cases[self.__currentCase] = kwargs
        self.__currentCase += 1


def getTestCases(fileName):
    with open(fileName) as inputFile:
        content = inputFile.read()
        lines = content.split('\n')
        lineNum = 0
        testCase = None
        for line in lines:
            if lineNum == 0:
                testCase = TestCase(int(line))
                lineNum += 1
            else:
                if line:
                    testCase.addTestCase(googlerese=str(line))
    return testCase

def main():
    languageMap = {}
    learningCases = [
        ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
        ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
        ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'),
        ('y qee', 'a zoo')
    ]
    alphabet = set(ch for ch in 'abcdefghijklmnopqrstuvwxyz')
    mappedAlphabet = set(ch for ch in 'abcdefghijklmnopqrstuvwxyz')
    for case in learningCases:
        for i in xrange(len(case[0])):
            languageMap[case[0][i]] = case[1][i]
            alphabet -= set(case[1][i])
            mappedAlphabet -= set(case[0][i])
    for _ in xrange(len(alphabet)):
        languageMap[mappedAlphabet.pop()] = alphabet.pop()

    caseResponseTemplate = 'Case #{0}: {1}\n'
    testCases = getTestCases('data/A-small-attempt1.in')
    with open('data/a_output.out', 'w') as outputFile:
        for numCase, case in testCases.cases.iteritems():
            response = ''.join(languageMap.get(ch, ch) for ch in case['googlerese'])
            outputFile.write(caseResponseTemplate.format(numCase + 1, response))


if __name__ == '__main__':
    main()
