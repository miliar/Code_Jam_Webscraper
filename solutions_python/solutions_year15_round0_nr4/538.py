import os, sys

#answers = (
#    (3, 2, 3),
#    (3, 3, 3),
#    (3, 3, 4),
#    (4, 4, 4),
#)

answers = {
   (1, 1, 1): True,
   (1, 1, 2): True,
   (1, 1, 3): True,
   (1, 1, 4): True,
   (1, 2, 1): True,
   (1, 2, 2): True,
   (1, 2, 3): True,
   (1, 2, 4): True,
   (1, 3, 1): True,
   (1, 3, 2): True,
   (1, 3, 3): True,
   (1, 3, 4): True,
   (1, 4, 1): True,
   (1, 4, 2): True,
   (1, 4, 3): True,
   (1, 4, 4): True,
   (2, 1, 1): False,
   (2, 1, 2): True,
   (2, 1, 3): False,
   (2, 1, 4): True,
   (2, 2, 1): True,
   (2, 2, 2): True,
   (2, 2, 3): True,
   (2, 2, 4): True,
   (2, 3, 1): False,
   (2, 3, 2): True,
   (2, 3, 3): False,
   (2, 3, 4): True,
   (2, 4, 1): True,
   (2, 4, 2): True,
   (2, 4, 3): True,
   (2, 4, 4): True,
   (3, 1, 1): False,
   (3, 1, 2): False,
   (3, 1, 3): False,
   (3, 1, 4): False,
   (3, 2, 1): False,
   (3, 2, 2): False,
   (3, 2, 3): True,
   (3, 2, 4): False,
   (3, 3, 1): False,
   (3, 3, 2): True,
   (3, 3, 3): True,
   (3, 3, 4): True,
   (3, 4, 1): False,
   (3, 4, 2): False,
   (3, 4, 3): True,
   (3, 4, 4): False,
   (4, 1, 1): False,
   (4, 1, 2): False,
   (4, 1, 3): False,
   (4, 1, 4): False,
   (4, 2, 1): False,
   (4, 2, 2): False,
   (4, 2, 3): False,
   (4, 2, 4): False,
   (4, 3, 1): False,
   (4, 3, 2): False,
   (4, 3, 3): False,
   (4, 3, 4): True,
   (4, 4, 1): False,
   (4, 4, 2): False,
   (4, 4, 3): True,
   (4, 4, 4): True
}

#nums = [0, 1, 1, 2, 5]

def answer(x, r, c):
    if answers[(x, r, c)] or answers[(x, c, r)]:
        return "GABRIEL"
    else:
        return "RICHARD"

#def answer(x, r, c):
#    if x == 1:
#        return "GABRIEL"
#
#    if x == 2:
#        if (r % 2 == 0) or (c % 2 == 0):
#            return "GABRIEL"
#        else:
#            return "RICHARD"
#
#    if (x > r) and (x > c):
#        return "RICHARD"
#
#    if (r * c) % x != 0:
#        return "RICHARD"
#
#    if ((x, r, c) in answers) or ((x, c, r) in answers):
#        return "GABRIEL"
#    else:
#        return "RICHARD"
#
lines = sys.stdin.read().split('\n')

lines.pop(0)

case = 0
for line in lines:
    if not line:
        break
    case += 1

    [x, r, c] = [int(a) for a in line.split()]

    print "Case #%d: %s" % (case, answer(x, r, c))
