#!/usr/bin/python
import sys

class II:
    def __init__(self,time,pos):
        self.time = time
        self.pos = pos


def seconds(line):
    sl = line.split()
    N = int(sl[0])
    sl = sl[1:]
    i = 0
    blue = []
    orange = []
    while i < N:
        if sl[i*2] == "B":
            blue.append(II(i,int(sl[i*2+1])))
        else:
            orange.append(II(i,int(sl[i*2+1])))
        i += 1
    bpos = 1
    opos = 1
    time = 0
    while len(blue) != 0 or len(orange) != 0:
        time += 1
        if len(blue) == 0:
            if orange[0].pos == opos:
                orange = orange[1:]
            elif orange[0].pos < opos:
                opos -=1
            else:
                opos += 1
        elif len(orange) == 0:
            if blue[0].pos == bpos:
                blue = blue[1:]
            elif blue[0].pos < bpos:
                bpos -= 1
            else:
                bpos += 1
        else:
            if orange[0].time < blue[0].time:
                if orange[0].pos == opos:
                    orange = orange[1:]
                elif orange[0].pos < opos:
                    opos -=1
                else:
                    opos += 1
                if blue[0].pos < bpos:
                    bpos -= 1
                elif blue[0].pos > bpos:
                    bpos += 1
            else:
                if blue[0].pos == bpos:
                    blue = blue[1:]
                elif blue[0].pos < bpos:
                    bpos -= 1
                else:
                    bpos += 1
                if orange[0].pos < opos:
                    opos -=1
                elif orange[0].pos > opos:
                    opos += 1
    return time

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    i = 0
    while i < T:
        i += 1
        line = sys.stdin.readline()
        print "Case #%s: %s" % (i, seconds(line))
