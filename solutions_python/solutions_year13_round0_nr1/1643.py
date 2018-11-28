#!/usr/bin/env python

def main():
    with open('input.txt') as f:
        input_ = f.readlines()
    input_ = [l.rstrip('\n') for l in input_ if l != '\n']
    total_T = int(input_[0])
    #print total_T
    for T in xrange(1,total_T+1):
        #print T
        map_ = []
        map_.append(input_[4*T-4+1])
        map_.append(input_[4*T-4+2])
        map_.append(input_[4*T-4+3])
        map_.append(input_[4*T-4+4])
        

        map_ = [[c for c in line] for line in map_]
        #print map_

        X_won = 0
        O_won = 0

        lines = [''.join(l) for l in map_]
        #print lines
        linesx = [''.join([map_[i][j] for i in xrange(4)]) for j in xrange(4)]
        #print linesx
        xlines = ''.join([map_[i][i] for i in xrange(4)])
        ylines = ''.join([map_[i][3-i] for i in xrange(4)])

        for l in lines+linesx+[xlines]+[ylines]:
            import re
            if re.search(r'[XT][XT][XT][XT]', l):
                X_won = 1
            if re.search(r'[OT][OT][OT][OT]', l):
                O_won = 1


        #print X_won, O_won
        if X_won == O_won:
            if any(['.' in l for l in lines]):
                print "Case #{}: Game has not completed".format(T)
            else:
                print "Case #{}: Draw".format(T)
        elif X_won:
            print "Case #{}: X won".format(T)
        else:
            print "Case #{}: O won".format(T)

            


if __name__ == '__main__':
    main()