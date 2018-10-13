#!/usr/bin/python
import sys

def dist(a,b):
    return abs(a-b)

def move(pos, dst, n_moves = 100000):
    if pos > dst:
        return pos - min(n_moves, dist(pos,dst))
    else:
        return pos + min(n_moves, dist(pos,dst))

T = int(sys.stdin.readline())
for test_case in range(T):
    args = sys.stdin.readline().strip().split()
    N = int(args[0])

    # [(turn, o_dst, b_dst)]
    DONE = None
    presses = []
    o_dst = b_dst = DONE
    for robot, location in zip(args[-2:0:-2], args[-1:1:-2]):
        if robot == 'O':
            o_dst = int(location)
        else:
            b_dst = int(location)
        presses.append((robot, o_dst, b_dst))

    presses.reverse()

    DEBUG = False

    orange = blue = 1
    step = 0
    time = 0
    while step < len(presses):
        turn, o_dst, b_dst = presses[step]
        if DEBUG:
            print 'time', time
            print 't', turn, 'o_dst', o_dst, 'b_dst', b_dst, 'o', orange, 'b', blue

        if turn == 'O':
            if orange == o_dst:
                if DEBUG:
                    print 'o pressed button'
                time += 1
                step +=1
                d = 1
            else:
                if DEBUG:
                    print 'o moving to ', o_dst, 'from', orange
                d = dist(orange, o_dst)
                orange = o_dst
                time += d

            if b_dst is not DONE:
                blue = move(blue, b_dst, d)
        else:
            if blue == b_dst:
                if DEBUG:
                    print 'blue pressed button'
                time += 1
                step +=1
                d = 1
            else:
                if DEBUG:
                    print 'b moving to ', b_dst, 'from', blue
                d = dist(blue, b_dst)
                blue = b_dst
                time += d

            if o_dst is not DONE:
                orange = move(orange, o_dst, d)

    if DEBUG:
        print

    print "Case #%d: %s" % (test_case + 1, time)
