#!/usr/bin/env python
import sys
fp = open("sample.txt")
nTestCases = int(fp.readline())
for i in range(0, nTestCases):
  testcase = []
  for j in range(0, 2):
    nAnswerRow = int(fp.readline())
    cards = []
    for k in range(0, 4):
      l = set(map(lambda x: int(x), fp.readline().strip().split()))
      if len(l) != 4:
        print "format wrong!"
      cards.append(l)

    testcase.append({"rownum": nAnswerRow, "cards": cards})

  if len(testcase) != 2:
    print "more inputs!!"
    continue

  answerlines = []
  for j in range(0, 2):
    answerlines.append(testcase[j]['cards'][testcase[j]['rownum']-1])

  answer = list(answerlines[0].intersection(answerlines[1]))
  if len(answer) == 1:
    print "Case #%d: %d" % (i+1, answer[0])
  elif len(answer) > 1:
    print "Case #%d: Bad magician!" % (i+1)
  elif len(answer) == 0:
    print "Case #%d: Volunteer cheated!" % (i+1)
