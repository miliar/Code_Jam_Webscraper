#!/usr/bin/env python

import sys, math

def getmin(seq, debug=False):

    lastp = {'O':1, 'B':1}

    last_type = ''
    last_wait = 0
    all = 0

    for s in seq:
        if debug:
            print s

        type = s[0]
        pos = int(s[1:])

        move = math.fabs(pos - lastp[type])

        if type != last_type: # last move is another type
            move -= last_wait
            if move < 0:
                move = 0

            t_last_wait = last_wait
            last_wait = 0 # type changed
        else:
            t_last_wait = last_wait

        last_type = type
        lastp[type] = pos
        last_wait += (move + 1)
        all += (move + 1)

        if debug:
            print "   %s move %d (%d=>%d, -%d) push 1" % (type, move, lastp[type], pos, t_last_wait)
            print "   all: %d" % all

    return all

def main():

    # getmin(['B2', 'B1'], True)
    # return
    
    if len(sys.argv) < 2:
        print "Usage: %s IN" % sys.argv[0]
        sys.exit(1)

    fin = open(sys.argv[1])
    cases = int(fin.readline().strip())

    for c in xrange(cases):
        line = fin.readline().split()
        moves = int(line.pop(0))
        
        seq = []
        for i in xrange(moves):
            type = line.pop(0)
            pos = line.pop(0)
            seq.append("%s%s" % (type, pos))

        print "Case #%d: %d" % (c+1, getmin(seq))


if __name__ == "__main__":
    main()
