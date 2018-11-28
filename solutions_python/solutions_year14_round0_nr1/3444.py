#!/usr/bin/env python
# -*- encoding: utf-8 -*-


def checkResults(testCase):
    ans1 = testCase[0][0]
    ans2 = testCase[5][0]
    matrix1 = testCase[1:5]
    matrix2 = testCase[6:]
    key = set(matrix1[ans1 - 1]) & set(matrix2[ans2 - 1])
    if len(key) == 1:
        return key.pop()
    elif len(key) > 1:
        return 'Bad magician!'
    else:
        return 'Volunteer cheated!'


def stripSplitLine(line):
    return map(int, line.strip().split())

CHUNK_SIZE = 10

inputFile = open('input.txt')
resultsFile = open('results.txt', 'w')

numCases = stripSplitLine(inputFile.readline())[0]

for i in range(numCases):
    lines = [stripSplitLine(inputFile.readline()) for _ in range(CHUNK_SIZE)]
    resultsFile.write('Case #{0}: {1}\n'.format(i+1, checkResults(lines)))
