import fileinput
import re

WHITESPACE = re.compile("\s+")

def readlines():
    for line in fileinput.input():
        yield map(int, WHITESPACE.split(line.strip()))



def problems():
    lines = readlines()
    (T, ) = lines.next()
    for p in range(T):
        (answer1,) = lines.next()
        possiblities = set([
            lines.next()
            for i in range(4)
        ][answer1 - 1])
        (answer2,) = lines.next()
        possiblities = possiblities.intersection([
            lines.next()
            for i in range(4)
        ][answer2 - 1])
        result = None
        if len(possiblities) == 0:
            result = "Volunteer cheated!"
        if len(possiblities) == 1:
            result = possiblities.pop()
        if len(possiblities) > 1:
            result = "Bad magician!"
        print "Case #%i: %s" % (p+1, result)

problems()