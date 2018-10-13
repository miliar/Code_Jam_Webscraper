#/bin/env python3

import unittest
import pdb
import fileinput
import re

def breadthFirstTreeSearch(initialState, nextStates, isWin):
    explored = set()
    toExplore = [(initialState, ())] # FIFO queue
    for state, parents in toExplore:
        if isWin(state):
            return (state, parents)
        explored.add(state)
        nextParents = (state,) + parents
        nexts = [(_next, nextParents) for _next in nextStates(state)
                    if _next not in explored]
        toExplore.extend(nexts)
    return (None, None)

def solvePancakeFlipper(initialState, flipperSize):
    if not isPossible(initialState, flipperSize):
        return "IMPOSSIBLE"
    simplifiedState, nSimplificationActions = simplifyState(initialState, flipperSize)
    state, parents = _solvePancakeFlipper(simplifiedState, flipperSize)
    if parents == None:
        return "IMPOSSIBLE"
    else:
        return len(parents) + nSimplificationActions

def isPossible(initialState, flipperSize):
    return len(set(initialState[-flipperSize:flipperSize])) <= 1

def simplifyState(initialState, flipperSize):
    return initialState, 0

def _solvePancakeFlipper(initialState, flipperSize):
    return breadthFirstTreeSearch(initialState, makeNextStates(flipperSize), makeIsWin(initialState))

def makeIsWin(initialState):
    winState = "+" * len(initialState)
    def isWin(state):
        return state == winState
    return isWin

def makeNextStates(flipperSize):
    def nextStates(state):
        if len(state) < flipperSize:
            return
        for i in range(len(state) - flipperSize + 1):
            yield flip(i, flipperSize, state)
    return nextStates

def flip(i, flipperSize, state):
    prefix = state[:i]
    suffix = state[(i + flipperSize):]
    flipped = state[i:(i + flipperSize)].translate(str.maketrans({"-": "+", "+": "-"}))
    return "{}{}{}".format(prefix, flipped, suffix)

class ContestTest(unittest.TestCase):
    def testEmptyWin(self):
        self.assertEqual(0, solvePancakeFlipper("", 18))

    def testTooShortWin(self):
        self.assertEqual(0, solvePancakeFlipper("+", 18))

    def testTooShortFail(self):
        self.assertEqual("IMPOSSIBLE", solvePancakeFlipper("-", 18))

    def testFlipperNotWorkingWin(self):
        self.assertEqual(0, solvePancakeFlipper("+", 0))

    def testFlipperNotWorkingFail(self):
        self.assertEqual("IMPOSSIBLE", solvePancakeFlipper("-", 0))

class OfficialTest(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(3, solvePancakeFlipper("---+-++-", 3))

    def testCase2(self):
        self.assertEqual(0, solvePancakeFlipper("+++++", 4))

    def testCase3(self):
        self.assertEqual("IMPOSSIBLE", solvePancakeFlipper("-+-+-", 4))

class IsImpossibleTest(unittest.TestCase):
    def possible(self):
        self.assertTrue(isPossible("--++--", 2))

    def testCase1(self):
        self.assertTrue(isPossible("---+-++-", 3))

    def impossible(self):
        self.assertTrue(not isPossible("--+---", 4))

    def nearImpossible(self):
        self.assertTrue(isPossible("--++--", 4))

class SimplifyStateTest(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(("---+-++-", 0), simplifyState("---+-++-", 3))


if __name__ == "__main__":
    nCases = int(input())
    for n, line in enumerate(fileinput.input()):
        if n == nCases:
            break
        m = re.match(r"([+-]+)\s+(\d+)\s*$", line)
        if not m:
            break
        initialState = m.group(1)
        flipperSize = int(m.group(2))
        print("Case #{}: {}".format(n + 1, solvePancakeFlipper(initialState, flipperSize)))
