#!/usr/bin/python2.6
#-*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    if not sys.argv[1:]:
        print "Usage: %s [input file]" % sys.argv[0]
        sys.exit(1)

    with open(sys.argv[1]) as f:
        num = int(f.readline())

        for i in range(1, num+1):
            # unpack values
            values = f.readline().split()
            snappers, toggles = int(values[0]), int(values[1])
            # calculate the result
            result = "ON" if bin(toggles)[-snappers:] == "1" * snappers else "OFF"
            # output
            print "Case #%s: %s" % (i, result)
