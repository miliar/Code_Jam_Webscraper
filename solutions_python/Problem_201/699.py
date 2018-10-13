#!/usr/bin/python3
from __future__ import print_function
import sys

debug = False

def onePersonChoosesOneStall(stalls, emptySeq):
    maxFree = max(emptySeq)
    posFirstMaxFree = emptySeq.index(maxFree)
    pos = maxFree // 2
    #~ print(maxFree, pos)
    if (maxFree % 2) == 1:
        return posFirstMaxFree, emptySeq[:posFirstMaxFree] + [pos,pos] + emptySeq[posFirstMaxFree+1:]
    else:
        return posFirstMaxFree, emptySeq[:posFirstMaxFree] + [pos-1,pos] + emptySeq[posFirstMaxFree+1:]
        

def peopleChooseStalls(people, stalls):
    emptySeq = [stalls]
    lastPos = -1
    for i in range(people):
        lastPos, emptySeq = onePersonChoosesOneStall(stalls, emptySeq)
    return max(emptySeq[lastPos],emptySeq[lastPos+1]), min(emptySeq[lastPos],emptySeq[lastPos+1]), emptySeq


def onePersonChoosesOneStallDict(stalls, emptySeq):
    maxFree = max(emptySeq)
    if debug: print(emptySeq)
    if emptySeq[maxFree] > 1:
        emptySeq[maxFree] -= 1
    else:
        emptySeq.pop(maxFree)
    Ls = maxFree // 2
    if (maxFree % 2) == 1:
        if Ls in emptySeq:
            emptySeq[Ls] += 2
        else:
            emptySeq[Ls] = 2
        return Ls, Ls, emptySeq
    else:
        if Ls in emptySeq:
            emptySeq[Ls] += 1
        else:
            emptySeq[Ls] = 1
        if Ls - 1 in emptySeq:
            emptySeq[Ls - 1] += 1
        else:
            emptySeq[Ls - 1] = 1
        return Ls, Ls - 1, emptySeq
        

def peopleChooseStallsDict(people, stalls):
    emptySeq = {stalls: 1}
    y = -1
    z = -1
    for i in range(people):
        y, z, emptySeq = onePersonChoosesOneStallDict(stalls, emptySeq)
        if y == 0:
            return 0, 0, {}
    return y, z, emptySeq


def peopleChooseStallsDirect(people, stalls):
    emptySeq = {stalls: 1}
    y = -1
    z = -1
    remainingPeople = people
    while remainingPeople > 0:
        maxFree = max(emptySeq)
        if debug: print(emptySeq)
        Ls = maxFree // 2
        if Ls == 0:
            return 0, 0, {}
        availablePlaces = emptySeq[maxFree]
        emptySeq.pop(maxFree)
        if availablePlaces > remainingPeople:
            if (maxFree % 2) == 1:
                y = Ls
                z = Ls
            else:
                y = Ls
                z = Ls - 1
            break
        else:
            if (maxFree % 2) == 1:
                y = z = Ls
                if Ls in emptySeq:
                    emptySeq[Ls] += 2 * availablePlaces
                else:
                    emptySeq[Ls] = 2 * availablePlaces
            else:
                y = Ls
                z = Ls - 1
                if Ls in emptySeq:
                    emptySeq[Ls] += availablePlaces
                else:
                    emptySeq[Ls] = availablePlaces
                if Ls - 1 in emptySeq:
                    emptySeq[Ls - 1] += availablePlaces
                else:
                    emptySeq[Ls - 1] = availablePlaces
        remainingPeople -= availablePlaces

    return y, z, emptySeq


lines = []
for line in sys.stdin:
    lines.append(line.rstrip('\n'))

n = int(lines[0])
for i in range(n):
    if debug: print('-' * 20)
    stalls, people = list(map(int, lines[i+1].split(' ')))
    if debug: print(stalls, people)
    #~ emptySeq = [stalls]
    #~ emptySeq = onePersonChoosesOneStall(stalls, emptySeq)
    #~ y, z, emptySeq = peopleChooseStallsDict(people, stalls)
    y, z, emptySeq = peopleChooseStallsDirect(people, stalls)
    if z < 0:
        z = 0
    if debug: print(emptySeq)
    print('Case #' + str(i+1) + ': ' + str(y) + ' ' + str(z))
