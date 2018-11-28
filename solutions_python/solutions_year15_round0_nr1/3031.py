#!/usr/bin/env python
import fileinput

def invited_clappers(levels):
    clapping = 0
    invited = 0
    for Si, Pi in enumerate(levels):
        if clapping < Si:
            delta = Si - clapping
            invited += delta
            clapping += delta
        clapping += Pi
    return invited

def main():
    f = fileinput.input()
    cases = int(f.readline())
    for case in xrange(1, cases+1):
        Smax, levels = f.readline().split()
        levels = map(int, list(levels))
        print "Case #%d: %d" % (case, invited_clappers(levels))

if __name__ == '__main__':
    main()
