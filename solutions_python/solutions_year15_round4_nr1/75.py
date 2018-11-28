#!/usr/bin/env python

from sys import stdin, stderr

T = int(stdin.readline())

def Solve(R, C, arrows):
    ret = 0
    for arrow in arrows:
        safe = False
        save = False
        for nearr in arrows:
            if arrow == nearr: continue
            if arrow[0] == nearr[0]:
                save = True
                if arrow[2] == '<' and arrow[1] > nearr[1]:
                    safe = True
                    break
                if arrow[2] == '>' and arrow[1] < nearr[1]:
                    safe = True
                    break
                pass
            if arrow[1] == nearr[1]:
                save = True
                if arrow[2] == '^' and arrow[0] > nearr[0]:
                    safe = True
                    break
                if arrow[2] == 'v' and arrow[0] < nearr[0]:
                    safe = True
                    break
                pass
            pass
        if not save: return "IMPOSSIBLE"
        if not safe: ret += 1
        pass
    return ret


for t in range(T):
    R, C = [int(wd) for wd in stdin.readline().split()]
    arrows = []
    for r in range(R):
        line = stdin.readline().strip()
        for c, wd in enumerate(line):
            if wd == ".": continue
            arrows.append([r, c, wd])
            pass
        pass

    print "Case #%d:" % (t+1),
    print Solve(R, C, arrows)
