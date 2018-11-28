# -*- coding: utf-8 -*-
import sys

def calcInvite(max_level, audience):
    surplus = 0
    invite = 0
    for i in xrange(max_level+1):
        if audience[i] == 0:
            if surplus > 0:
                surplus -= 1
            else:
                invite += 1
        else:
            surplus += audience[i] - 1

    return invite

if __name__ == "__main__":
    f = open(sys.argv[1], 'r')
    test_num = int(f.readline())

    for i in xrange(1, test_num+1):
        line = f.readline().split()
        ans = calcInvite(int(line[0]), map(int, line[1]))
        print('Case #%i: %s' % (i, ans) )
