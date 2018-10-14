#!/usr/bin/env python
import sys
from pprint import pprint

# get the number of test cases as an int
numCases = int(sys.stdin.readline().replace("\n", ""))

answerString = "Case #%d: %s"

for case in range(numCases):
    # Parse board 1 and 2
    row1 = int(sys.stdin.readline().replace("\n", ""))
    board1 = []
    for row in range(4):
        board1.append(set(int(card) for card in sys.stdin.readline().replace("\n", "").split()))

    row2 = int(sys.stdin.readline().replace("\n", ""))
    board2 = []
    for row in range(4):
        board2.append(set(int(card) for card in sys.stdin.readline().replace("\n", "").split()))

    # Get the intersection of the pointed-at rows. This is the cards that appear in both
    answer = board1[row1-1] & board2[row2-1]

    answerLen = len(answer)

    if answerLen == 0:
        print answerString %(case+1, "Volunteer cheated!")
    elif answerLen == 1:
        print answerString %(case+1, answer.pop())
    else:
        print answerString %(case+1, "Bad magician!")
