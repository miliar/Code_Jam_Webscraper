import math
import random

infilename = 'sample.txt'
infilename = 'B-small-attempt0.in'
#infilename = 'B-large.in'
outfilename = "output.txt"

with open(infilename, 'r') as infile:
    with open(outfilename, 'w') as outfile:
        t = int(infile.readline().strip())
        for test in range(1, t+1):
            outfile.write('Case #' + str(test) + ': ')
            line = infile.readline().strip()
            n = [int(x) for x in line.split()]
            b = [bin(int(x)) for x in n]
            win = 0
            for i in range(n[0]):
                for j in range(n[1]):
                    x = i & j
                    if x < n[2]:
                        win += 1
            outfile.write(str(win) + '\n')