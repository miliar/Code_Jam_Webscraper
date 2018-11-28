#!/usr/bin/python -w

from sys import stdin
import re

cases = stdin.readline()

for case_no in range(int(cases)):
    line = map(int,stdin.readline().rsplit(" "))
    N = line.pop(0)
    S = line.pop(0)
    p = line.pop(0)

    above_scores = [] #really only need a count
    for score_sum in (line):
        score = [score_sum/3 for x in range(3)]
        residual = score_sum - sum(score)
        lcv = 0
        while(residual):
            score[lcv] += 1
            residual -= 1
            lcv += 1

        max_p = max(score)
        if(max_p >= p):
            above_scores.append(score)
        elif(S and score_sum >= p and max_p+1 >= p and (lcv > 1 or lcv == 0)):
            score[0] += 1
            score[1] -= 1
            above_scores.append(score)
            S -= 1

    print "Case #"+str(case_no+1)+": "+str(len(above_scores))
