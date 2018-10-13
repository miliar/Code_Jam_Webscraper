#!/usr/bin/env python

import sys

def loadFile(filename):
    games = []
    no_games = 0
    with open(filename, 'r') as infile:
        no_games = int(infile.readline().strip())
        outputfilename = filename.split('.')[0] + '.out'
        with open(outputfilename, 'w') as outfile:
            for i in range(no_games):
                game = [int(j) for j in infile.readline().strip().split(' ')]
                s = getscore(game)
                outfile.write("Case #%d: %d\n"%(i+1, s))
                
def getscore(game):
    A = game[0]
    B = game[1]
    K = game[2]
    score = 0
    for a in range(A):
        for b in range(B):
            c = a&b
            if c < K:
                score += 1
    return score

if __name__ == '__main__':
    inputfilename = sys.argv[1]
    loadFile(inputfilename)
    