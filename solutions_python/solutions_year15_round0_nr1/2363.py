from sys import stdin
from itertools import count

def main():
    next(stdin)
    for (casenum, line) in zip(count(1), stdin):
        left, right = line.rstrip('\n').split(' ')
        maxshy = int(left)
        shycounts = [int(snum) for snum in right]
        output = case(maxshy, shycounts)
        print "Case #%d:" % casenum, output

def case(maxshy, shycounts):
    people = []
    for shy, num in zip(count(), shycounts):
        for i in xrange(num): people.append(shy)
        extras = 0
    reqshy = 0
    for shy in people:
        # print reqshy, shy
        if shy > reqshy:
            extras += (shy - reqshy)
            reqshy = shy + 1
        else:
            reqshy += 1
    return extras

if __name__ == '__main__':
    main()
