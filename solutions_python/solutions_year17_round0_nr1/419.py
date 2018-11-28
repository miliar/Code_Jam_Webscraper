# -*-coding:utf-8 -*

# import math
# from operator import itemgetter
# from fractions import Fraction
# from functools import lru_cache


def flip(S, K, p):
    return "".join(s if (i < p or i >= K + p) else ('+' if s == '-' else '-') for (i, s) in enumerate(S))


def main_func(S, K):
    res = 0
    for i in range(len(S) - K + 1):
        # print(S)
        if S[i] == '-':
            S = flip(S, K, i)
            res += 1
    if all(s == '+' for s in S):
        return str(res)
    else:
        return 'IMPOSSIBLE'

# print(main_func())

# ------------------------------------------------------------------------------------------------------------------------------
# We apply mainFunc to each input
# ------------------------------------------------------------------------------------------------------------------------------

hl = 1  # "Header lines" :Number of lines at the beginning of the input file (header information)
lpc = 1  # "Lines per test case" number of lines for each entry of input
# (lpc will be used only if that number is the same for every case)
lineSep = "\n"  # Line separator
colSep = " "  # column separator

with open("input.txt", 'r') as inputFile:
    # ------------------------------------------------------------------------------------------------------------
    # Parsing the input
    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------
    # Parsing the header
    # ------------------------------------------------------------------------
    inputLines = inputFile.read().split(lineSep)
    while inputLines[-1] == '': del inputLines[-1]  # Deleting all empty lines at the end
    T = int(inputLines[0])  # Number of test cases
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # Parsing the body
    # ------------------------------------------------------------------------
    caseStartIndex = [hl]
    for i in range(T):  # caseStartIndex[T] = 1 + index of the last line
        # (ie : the index where would start case T+1 if it existed). In most cases we won't use it.
        nbLinesForThisCase = lpc
        # nbLinesForThisCase = int(inputLines[caseStartIndex[i]]) + 1
        caseStartIndex.append(caseStartIndex[i] + nbLinesForThisCase)
    # ------------------------------------------------------------------------

    # ------------------------------------------------------------------------
    # Formatting the input so that it's ready to be passed to mainFunc(*input)
    # ------------------------------------------------------------------------
    formattedInput = \
        [
            [
                inputLines[caseStartIndex[caseID]].split(colSep)[0],
                int(inputLines[caseStartIndex[caseID]].split(colSep)[1])
            ]
            for caseID in range(T)
        ]
    # ------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------------------------------------
    # Generating the output : Apply mainFunc() to each test case
    # ------------------------------------------------------------------------------------------------------------
    outputString = "\n".join(["Case #"+str(i+1)+": "+main_func(*inp) for i, inp in enumerate(formattedInput)])
    print("output:")
    print(outputString)
    with open("output.txt", "w") as outputFile:
        outputFile.write(outputString)
    # ------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------