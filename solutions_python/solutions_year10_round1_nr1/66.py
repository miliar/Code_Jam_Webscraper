#!/usr/bin/env python
#By Jai Dhyani

import math, sys

def getints(f):
    return [int(x) for x in f.readline().split()]

def solve( x ):
    return 0

def find_matches(board, k):
    winners = {'R':False,'B':False}
    for i in xrange(len(board)):
        for j in xrange(len(board)):
            if board[i][j]=='.':
                continue
            target = board[i][j]
            if i+k<=len(board):
                matches = [ board[i+x][j] for x in xrange(k) if
                           board[i+x][j]==target]
                print matches,k
                if len(matches)==k:
                    winners[target]=True
                    continue
            if j+k<=len(board):
                matches = [ board[i][j+x] for x in xrange(k) if
                           board[i][j+x]==target]
                print matches,k
                if len(matches)==k:
                    winners[target]=True
                    continue
            if i+k<=len(board) and j+k<=len(board):
                matches = [ board[i+x][j+x] for x in xrange(k) if
                           board[i+x][j+x]==target]
                print matches,k
                if len(matches)==k:
                    winners[target]=True
                    continue
            if i-k>=-1 and j+k<=len(board):
                matches = [ target for x in xrange(k) if
                           board[i-x][j+x]==target]
                print matches,k
                if len(matches)==k:
                    winners[target]=True
                    continue
    return winners

if __name__ == '__main__':
    # filename=sys.argv[1]
    filename='A-large.in'
    outname=filename+'.out'
    f=open(filename)
    out=open(outname,'w')
    try:
        numtrials = getints(f)[0]
    except IndexError as ie:
        print 'no input data in %s'%filename
        exit(0)
    for i in xrange(numtrials):
        n,k = getints(f)
        print n,k
        board = []
        for l in xrange(n):
            row = [c for c in f.readline()[:-1] if not c=='.']
            row = ['.']*(n-len(row))+row
            board.append(row)
        for x in board:
            print x
        winners = find_matches(board, k)
        if winners['R']==False and winners['B']==False:
            answer = 'Neither'
        elif winners['R']==False and winners['B']==True:
            answer ='Blue'
        elif winners['R']==True and winners['B']==False:
            answer ='Red'
        else:
            answer = 'Both'
        answer_str = "Case #%d: %s"%(i+1,answer)
        print(answer_str)
        out.write(answer_str+'\n')

