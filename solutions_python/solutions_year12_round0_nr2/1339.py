#!/usr/bin/env python

import sys

if __name__ == "__main__":

    f = open("B-small-attempt0.in", 'r')      # input file
    fout = open("output", "w")  # output file

    T = int(f.readline())       # T test cases

    for t in xrange(T):
        line = f.readline().replace('\n', '').split(' ')     # read in a line and split it
        output = "Case #" + str(t+1) + ": " # Case #T: ...
        N = int(line[0])                    # number of Googlers
        S = int(line[1])                    # number of surprising tirplets of scores
        p = int(line[2])
        num = 0                 # the max num of Googlers that could have had a best result of at least p

        for n in xrange(N):
            score = int(line[n+3]) # get the score
            if score < 3 and p >= 1:
                continue
            if score % 3 == 0:
                x = score/3
                if x >= p:
                    num += 1
                elif (x+1 >= p) and (S > 0):
                    num += 1
                    S -= 1

            elif score % 3 == 1:
                x = score/3
                if x >= p or x+1 >= p:
                    num += 1

            elif score % 3 == 2:
                x = score/3
                if x >= p or x+1 >= p:
                    num += 1
                elif (x+2 >= p) and (S > 0):
                    num += 1
                    S -= 1


        output = output + str(num) + '\n'


        # if %s == 0: x x x
        #  if x >= 8: then fine
        #  else if x+1 > = 8: then x-1 x x+1 S--
        # if %s != 0: x x+1 x+1  p
        #  if x >= 8 then fine
        #  else if x+1 >= 8: then fine
        #  else if x+2 >=8: then x x x+2, S--
        # if %s == 1: x x x+1
        #

        fout.write(output)

