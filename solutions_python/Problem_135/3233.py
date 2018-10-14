#!/usr/bin/python
import sys
with open('game.txt') as f:
    content = f.readlines()
content = map(lambda s: s.strip(), content)
content = filter(None, content)
rowcard_one = 1
rowcard_two = 1
rval_one = [0 for x in xrange(4)]
rval_two = [0 for x in xrange(4)]
c_one = 0
c_two = 0
match = 0
case = 1
for line in content:
    if c_one == 0:
        c_one = int(line)
        continue
    else:
        if all(v == 0 for v in rval_one):
            if c_one == rowcard_one:
                rval_one = [int(i) for i in line.split()]
                rowcard_one += 1
            else:
                rowcard_one += 1
                continue
        else:
            if rowcard_one != 5:
                rowcard_one += 1
                continue
            else:
                if c_two == 0:
                    c_two = int(line)
                    continue
                else:
                    if all(v == 0 for v in rval_two):
                        if c_two == rowcard_two:
                            rval_two = [int(i) for i in line.split()]
                            rowcard_two += 1
                        else:
                            rowcard_two += 1
                            continue
                    if rowcard_two != 5:
                        rowcard_two += 1
                        continue
                    else:
                        for x in xrange(4):
                            for y in xrange(4):
                                if rval_one[x] == rval_two[y]:
                                    vmatch = rval_one[x]
                                    match += 1
                        if match > 1:
                            sys.stdout.write("Case #%d: Bad magician!\n" % (case))
                        if match == 1:
                            sys.stdout.write("Case #%d: %d\n" % (case,vmatch))
                        if match == 0:
                            sys.stdout.write("Case #%d: Volunteer cheated!\n" % (case))
                        case += 1
                        c_one = 0
                        c_two = 0
                        match = 0
                        rowcard_one = 1
                        rowcard_two = 1
                        rval_one = [0 for x in xrange(4)]
                        rval_two = [0 for x in xrange(4)]
