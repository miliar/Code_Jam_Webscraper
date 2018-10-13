#!/usr/bin/env python
import sys

def main():
    f = sys.stdin
    cases = int(f.readline())
    for case in range(1, cases+1):
        possible = set()
        not_possible = set()
        for trial in range(2):
            volunteer_row = int(f.readline())
            for row in range(1,5):
                line = set([ int(n) for n in  f.readline().split(" ")])
                if row == volunteer_row:
                    possible.update(line)
                else:
                    not_possible.update(line)

        possible.difference_update(not_possible)

        if len(possible) == 1:
            print "Case #%s: %s" % (case, possible.pop())
        elif len(possible) == 0:
            print "Case #%s: %s" % (case, "Volunteer cheated!")
        else:
            print "Case #%s: %s" % (case, "Bad magician!")
            
if __name__ == "__main__":
    main()
