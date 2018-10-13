#!/usr/bin/env python

from sys import stdin

EXHAUSTED = {}

def pos(vine):
    return vine[0]

def length(vine):
    return vine[1]

def exhausted(vine):
    return vine[2]

def mkvine(pos,length):
    return (pos,length)

def vines_in_range(vines, current, at):
    for vine in vines:
        if pos(vine) <= pos(current):
            continue
        if (vine,at) in EXHAUSTED:
            continue
        if pos(vine) <= 2*pos(current) - at:
            yield vine

def love_in_range(current, at, ledge):
    return 2*pos(current)-at >= ledge

def search(vines, current, at, ledge):
    """
    >>> vines = [mkvine(3,4),mkvine(4,10),mkvine(6,10)]
    >>> search(vines, vines[0], 0, 9)
    True
    >>> vines = [mkvine(3,4),mkvine(4,10),mkvine(7,10)]
    >>> search(vines, vines[0], 0, 9)
    False
    """
#    print vines
#    print current
#    print ledge
    if love_in_range(current, at, ledge):
#        print current
#        print 1
        return True
    for vine in vines_in_range(vines, current, at):
#        print vine
        if length(vine) <= pos(vine)-pos(current):
            new_at = pos(vine)-length(vine)
        else:
            new_at = pos(current)
        if love_in_range(vine, new_at, ledge):
#            print vine
            return True
        else:
#            print new_at
            if search(vines, vine, new_at, ledge):
                return True
    EXHAUSTED[(current,at)] = True
    return False

def main():
    T = int(stdin.readline())
    for t in range(T):
        EXHAUSTED = {}
        N = int(stdin.readline())
        vines = []
        for n in range(N):
            [p,l] = [int(x) for x in stdin.readline().split()]
            vines.append(mkvine(p,l))
        ledge = int(stdin.readline())
        if search(vines[1:], vines[0], 0, ledge):
            print "Case #%d: YES" % (t+1)
        else:
            print "Case #%d: NO" % (t+1)
            

if __name__ == "__main__":
    main()
