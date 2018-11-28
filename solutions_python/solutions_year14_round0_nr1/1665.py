#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

def next_answer(f):
    "return the row"
    answ1 = int(f.readline())
    lines = []
    row   = set()
    for i in range(1, 5):
        if i == answ1:
            row = set(map(int, f.readline().replace('\n', '').split(' ')))
        else:
            f.readline()
    return row

def next_turn(f):
    t1 = next_answer(f)
    t2 = next_answer(f)
    pos = t1.intersection(t2)
    n = len(pos)

    if n == 0:
        return 'Volunteer cheated!'
    elif n == 1:
        return str(pos.pop())
    else:
        return 'Bad magician!'

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "usage: %s <input file>" % sys.argv[0]
        sys.exit(1)

    with open(sys.argv[1]) as f:
        with open("%s.out" % sys.argv[1], 'w') as out:
            c = int(f.readline())
            for i in range(1, c+1):
                out.write('Case #%d: %s\n' % (i, next_turn(f)))
    print 'done.'
