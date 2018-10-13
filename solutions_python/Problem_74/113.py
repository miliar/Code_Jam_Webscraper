#!/usr/bin/python

import sys;

def main():
    numCases = int(sys.stdin.readline().strip());
    for iCase in range(0, numCases):
        fields = sys.stdin.readline().strip().split();
        N = int(fields[0]);
        if len(fields) != N*2 + 1:
            print >>sys.stderr, "invalid input case ", iCase;
            sys.exit(1);

        orange = (1, 0);
        blue = (1, 0);
        last = 0;

        for i in range(0, N):
            c = fields[i*2 + 1];
            p = int(fields[i*2 + 2]);

            if c == 'O':
                orange = (p, max(last + 1, orange[1] + abs(p - orange[0]) + 1));
                last = orange[1];
            elif c == 'B':
                blue = (p, max(last + 1, blue[1] + abs(p - blue[0]) + 1));
                last = blue[1];
            else:
                print >>sys.stderr, "invalid code ", c, " on case ", iCase;
                sys.exit(1);

        print "Case #%d: %d" % (iCase + 1, last);


main();

