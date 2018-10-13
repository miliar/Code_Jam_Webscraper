#!/usr/bin/python

import re
import sys

def main():
    sys.stdin.readline()
    for tcNum, line in enumerate(sys.stdin.readlines()):
        name, n = line.split()[0], int(line.split()[1])
        nValue = 0
        for i in xrange(len(name)):
            for j in xrange(i+1, len(name)+1):
                ss = [s for s in re.split("[aeiou]", name[i:j]) if len(s) >= n]
                if len(ss) > 0:
                    nValue += 1
        print "Case #%d: %d" % (tcNum + 1, nValue)

if __name__ == "__main__":
    main()
