#!/usr/bin/env python

import os, sys
import codejam

def bottrust(testcase):
    if len(testcase) != 1:
        raise RuntimeError, "Oops, we got a bad testcase!"
    botlist = testcase[0].split(" ")
    botsize = int(botlist[0])
    if len(botlist) != 2*botsize+1:
        raise RuntimeError, "Oops, we got %d items when we were told %d" % (len(botlist), 2*botsize+1)
    # Let's figure out who's pressing what in what order.
    BLUE = 0
    ORANGE = 1
    targetlist = [[], []]
    for i in range(botsize):
        if botlist[2*i+1] == 'O':
            targetlist[ORANGE].append((i, int(botlist[2*i+2])))
        elif botlist[2*i+1] == 'B':
            targetlist[BLUE].append((i, int(botlist[2*i+2])))
    time = 0
    pressed = 0
    locations = [1, 1]
    pending_pressed = False
    while pressed < botsize:
        for bot in range(2):
            # See what the bot should do.
            if len(targetlist[bot]):
                (botordinal, bottarget) = targetlist[bot][0]
                #print "Time %d: bot %d at %d, looking for ord %d target %d" % (time, bot, locations[bot], botordinal, bottarget)
                if locations[bot] < bottarget:
                    # Move towards the target.
                    locations[bot] += 1
                elif locations[bot] > bottarget:
                    # Move down towards the target.
                    locations[bot] -= 1
                elif botordinal == pressed:
                    # Press the button.
                    targetlist[bot].pop(0)
                    pending_pressed = True
                else:
                    # Do nothing and wait for the other guy to press the button.
                    pass
        time += 1
        if pending_pressed:
            pending_pressed = False
            pressed += 1

    return "%d" % time

if __name__ == "__main__":
    codejam.main(sys.argv[1:], bottrust, 1)
