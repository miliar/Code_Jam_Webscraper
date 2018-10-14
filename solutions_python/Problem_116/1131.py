from sys import stdin


def won(a, c):
    a = [x.replace("T", c) for x in a]
    ans = c * 4
    if any(ans == x for x in a):
        return True

    if ans == "".join(a[i][i] for i in xrange(4)):
        return True
    if ans == "".join(a[3-i][i] for i in xrange(4)):
        return True
    if ans in ["".join(a[i][j] for i in xrange(4)) for j in xrange(4)]:
        return True
    return False



n = int(stdin.readline())
for tc in xrange(1, n + 1):
    a = [stdin.readline().strip() for _ in xrange(4)]
    print "Case #{0}:".format(tc),
    if won(a, "X"):
        print "X won"
    elif won(a, "O"):
        print "O won"
    elif any(x.find(".") != -1 for x in a):
        print "Game has not completed"
    else:
        print "Draw"
    stdin.readline()
