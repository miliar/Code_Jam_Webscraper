#!/usr/bin/env python
#
#  Solving Problems
#  ================
#
#  Jose Ignacio Galarza (igalarzab)
#  <igalarzab@gmail.com>
#  http://sysvar.net
#

import sys

def solve(reductions, deletions, letters, debug=False):
    s = letters[0]
    i = 1

    while i < len(letters[1:])+1:
        s += letters[i]
        make_reductions = True

        # Reductions
        try:
            while make_reductions:
                if reductions.has_key(s[-1]+s[-2]):
                    s = s[:-2] + reductions[s[-1]+s[-2]]
                elif reductions.has_key(s[-2]+s[-1]):
                    s = s[:-2] + reductions[s[-2]+s[-1]]
                else:
                    make_reductions = False
        except:
            pass

        for deletion in deletions:
            if deletion[0] in s and deletion[1] in s:

                try:
                    i += 1
                    s = letters[i]
                except:
                    s = ''

                break
        i += 1

    # Convert format
    r = str([str(i) for i in s])
    return r.replace("'", "")


if __name__ == '__main__':
    cases = int(sys.stdin.readline())

    for i in xrange(cases):
        line = sys.stdin.readline().split()
        reductions = {}
        deletions = []

        for j in xrange(1, int(line[0]) + 1):
            reductions[line[j][0:2]] = line[j][2]

        offset = 1 + int(line[0])
        for j in xrange(offset+1, offset + int(line[offset]) + 1):
            deletions.append(line[j])

        offset += 1 + int(line[offset])
        print("Case #%d: %s" % (i+1, solve(reductions, deletions, line[offset+1])))

# vim: ai ts=4 sts=4 et sw=4
