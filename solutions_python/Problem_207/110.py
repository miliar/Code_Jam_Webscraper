import glob, pprint, pickle, os, time, sys
from copy import copy
import heapq
from numpy import array, sin, cos, zeros
import itertools
import math
import numpy as np
import bisect

RED, ORANGE, YELLOW, GREEN, BLUE, VIOLET = "R","O","Y","G","B","V"
def solve(N, R, O, Y, G, B, V):
    print N, R, O, Y, G, B, V
    # orange only borders blue, green only borders red, violet only borders yellow

    #greedy
    answer = []

    # bluestring
    if O!=0:
        bluestring = "B"
        B-=1
        while O>0:
            bluestring+="O"
            O -=1
            if B>0:
                B -=1
                bluestring+="B"
            elif all(np.array([R, O, Y, G, B, V]) == 0):
                return bluestring
            else:
                return None
        B+=1
    else:
        bluestring = ""


    if G!=0:
        redstring = "R"
        R-=1
        while G>0:
            redstring+="G"
            G -=1
            if R>0:
                R -=1
                redstring+="R"
            elif all(np.array([R, O, Y, G, B, V]) == 0):
                return redstring
            else:
                return None
        R+=1
    else:
        redstring = ""

    if V!=0:
        yellowstring = "Y"
        Y-=1
        while V>0:
            yellowstring+="V"
            V -=1
            if Y>0:
                Y -=1
                yellowstring+="Y"
            elif all(np.array([R, O, Y, G, B, V]) == 0):
                return yellowstring
            else:
                return None
        Y += 1
    else:
        yellowstring = ""

    if any(np.array([R, O, Y, G, B, V]) < 0):
        return None

    while sum([R, Y, B]) > 1:
        if any(np.array([R, O, Y, G, B, V]) < 0):
            return None

        if R==max([R,Y,B]):
            if not answer or answer[-1]!=RED:
                R-=1
                answer.extend([RED])
            else:
                if Y==max([Y,B]):
                    Y-=1
                    answer.extend([YELLOW])
                else:
                    B-=1
                    answer.extend([BLUE])
            continue

        if Y==max([R,Y,B]):
            if not answer or answer[-1]!=YELLOW:
                Y-=1
                answer.extend([YELLOW])
            else:
                if R==max([R,B]):
                    R-=1
                    answer.extend([RED])
                else:
                    B-=1
                    answer.extend([BLUE])
            continue


        if B==max([R,Y,B]):
            if not answer or answer[-1]!=BLUE:
                B-=1
                answer.extend([BLUE])
            else:
                if R==max([R,Y]):
                    R-=1
                    answer.extend([RED])
                else:
                    Y-=1
                    answer.extend([YELLOW])
            continue


    answer = "".join(answer)
    print answer, R,Y,B

    # add the last one, somewhere in the string

    if R>0:
        if not answer:
            answer = "R"
        if answer[0]!=RED:
            answer += "R"
        else:
            try:
                idx = answer.index("BY")
                answer = answer[:idx+1] + "R" + answer[idx+1:]
            except ValueError:
                try:
                    idx = answer.index("YB")
                    answer = answer[:idx+1] + "R" + answer[idx+1:]
                except ValueError:
                    return None

    if B>0:
        if not answer:
            answer = "B"
        if answer[0]!=BLUE:
            answer += "B"
        else:
            try:
                idx = answer.index("RY")
                answer = answer[:idx+1] + "B" + answer[idx+1:]
            except ValueError:
                try:
                    idx = answer.index("YR")
                    answer = answer[:idx+1] + "B" + answer[idx+1:]
                except ValueError:
                    return None


    if Y>0:
        if not answer:
            answer = "Y"
        if answer[0]!=YELLOW:
            answer += "Y"
        else:
            # find a spot between a blue and yellow
            try:
                idx = answer.index("RB")
                answer = answer[:idx+1] + "Y" + answer[idx+1:]
            except ValueError:
                try:
                    idx = answer.index("BR")
                    answer = answer[:idx+1] + "Y" + answer[idx+1:]
                except ValueError:
                    return None

    print answer
    if redstring:
        answer = answer.replace("R", redstring, 1)
    if bluestring:
        answer = answer.replace("B", bluestring, 1)
    if yellowstring:
        answer = answer.replace("Y", yellowstring, 1)
    # assert len(answer)==N
    return answer



output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    def read_frac():
        return [int(x) for x in f.readline().strip().split('/')]
    def read_strs():
        return [x for x in f.readline().strip().split(' ')]
    def read_floats():
        return [float(x) for x in f.readline().strip().split(' ')]
    def read_cakes():
        return [True if x=='+' else False for x in f.readline().strip()]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        N,R, O, Y, G, B, V = read_ints()
        answer = solve(N, R, O, Y, G, B, V)

        ### output ###
        if answer is None:
            answer = "IMPOSSIBLE"
        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()