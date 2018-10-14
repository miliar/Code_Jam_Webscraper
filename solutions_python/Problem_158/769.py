#
if __name__ == "__main__":
    f = open('qr4.in')
    out = open('qr4.out', 'w')
    nTestCase = int(f.readline().rstrip())
    G = "GABRIEL"
    R = "RICHARD"
    for testCase in range(nTestCase):
        sx,sr,sc = f.readline().rstrip().split(' ')
        x = int(sx)
        r = int(sr)
        c = int(sc)
        if r * c < x:
            winner = R
        elif r * c == x:
            if x < 3:
                winner = G
            else:
                winner = R
        elif r * c % x != 0:
            winner = R
        else:
            if r * c % x == 0 and x == 4 and ( r < 3 or c < 3 ):
                winner = R
            else:
                winner = G
        print "Case #%s: %s %s %s %s\n" % (testCase + 1, winner, x, r, c)
        out.write("Case #%s: %s\n" % (testCase + 1, winner))

