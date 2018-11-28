#!/usr/bin/python

import sys

num_cases = int(sys.stdin.readline())

for i in range(num_cases):
    raw_info = sys.stdin.readline().split()
    X = int(raw_info[0])
    R = int(raw_info[1])
    C = int(raw_info[2])
    winner = str()
    #broad criteria
    #Richard winning means grid can be beat
    if(X >= 7):
        winner = "Richard"
        print 'Case #{}: {}'.format(i+1, winner)
        continue
    if((R*C + X) % X != 0):
        winner = "Richard"
        print 'Case #{}: {}'.format(i+1, winner)
        continue
    if(R < X and C < X):
        winner = "Richard"
        print 'Case #{}: {}'.format(i+1, winner)
        continue
    if(R < X or C < X):
        if((X+2) % 2 == 0): #even X
            fatty = X/2
        else:
            fatty = (X+1)/2
        if(fatty > min(R, C)):
            winner = "Richard"
            print 'Case #{}: {}'.format(i+1, winner)
            continue
        if(fatty == min(R,C)):
            if(X > 3 and X < 6):
                winner = "Richard"
                print 'Case #{}: {}'.format(i+1, winner)
                continue

    winner = "Gabriel"
    print 'Case #{}: {}'.format(i+1, winner)


