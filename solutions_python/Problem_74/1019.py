#!/usr/bin/env python

import sys

#debug=True
debug=False
#adebug=True
adebug=False

def otherrobot (me):
    if me == "O": return "B"
    else: return "O"

def solve (seq,ro):
    if debug: print "Sequence",seq
    if debug: print "Robot order", ro
    ttime = 0
    pos = { "O":1, "B":1 }
    pop = "N"
    while len(seq["O"]) > 0 or len(seq["B"]) > 0:
        if debug: print "Robot order", ro
        ttime += 1
        for mycolor in ["O", "B"]:
            mypos = pos[mycolor]
            try:
                mynext = seq[mycolor][0]
            except IndexError:
                if adebug: print "%d: %s stay at button %d" % (ttime, mycolor, mypos)
                continue
            myturn = True if ro[0] == mycolor else False
            if debug: print mycolor, mypos, mynext, myturn
            if myturn and mynext == mypos:
                if adebug: print "%d: %s push button %d" % (ttime, mycolor, mypos)
                pop = mycolor
            elif mynext == mypos:
                if adebug: print "%d: %s stay at button %d" % (ttime, mycolor, mypos)
                pass
            elif mynext > mypos:
                if adebug: print "%d: %s move to button %d" % (ttime, mycolor, mypos+1)
                pos[mycolor] += 1
            elif mynext < mypos:
                if adebug: print "%d: %s move to button %d" % (ttime, mycolor, mypos-1)
                pos[mycolor] -= 1
            else:
                print "Something strange"
        if pop != "N":
            seq[pop].pop(0)
            ro.pop(0)
            pop = "N"


    return ttime

inputf = sys.stdin
inp = inputf.readlines()

totalinp = int(inp[0].strip())

if debug:
    print inp
    print totalinp
    print 

for i in xrange(1,totalinp+1):
    seq = { "B": [], "O": [] }
    ro = []

    cinps = inp[i].strip()
    cinpl = cinps.split(" ")
    if debug: print cinpl
    cinpcount = int(cinpl[0])
    cinp = cinpl[1:]
    for j in xrange (cinpcount):
        qtype = cinp[0]
        buttonno = int(cinp[1])
        ro.append(qtype)
        if qtype == "O": seq["O"].append(buttonno)
        else: seq["B"].append(buttonno)
        cinp = cinp[2:]

    print "Case #%d: %s" % (i , solve(seq,ro))
        



