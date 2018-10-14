import math
import sys

t = int(sys.stdin.readline())
for e in xrange(1, t+1):
    ans1 = int(sys.stdin.readline())
    board = [sys.stdin.readline().strip() for i in xrange(4)]
    s1 = set(map(int, board[ans1-1].split()))

    ans2 = int(sys.stdin.readline())
    board = [sys.stdin.readline().strip() for i in xrange(4)]
    s2 = set(map(int, board[ans2-1].split()))

    print "Case #{}:".format(e),
    if not s1 & s2:
        print "Volunteer cheated!"
    elif len(s1 & s2) == 1:
        print list(s1 & s2)[0]
    else:
        print "Bad magician!"

