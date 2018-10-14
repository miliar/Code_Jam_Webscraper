import sys

inputf = open("A-large.in")
lines = inputf.readlines()
s = []
i = 1
for l in lines[1:]:
    if l != "\n":
        s.append(l.strip())
    else:
        l10 = set([s[0][0], s[1][0], s[2][0], s[3][0]])
        l11 = set([s[0][1], s[1][1], s[2][1], s[3][1]])
        l12 = set([s[0][2], s[1][2], s[2][2], s[3][2]])
        l13 = set([s[0][3], s[1][3], s[2][3], s[3][3]])
        l20 = set([s[0][0], s[0][1], s[0][2], s[0][3]])
        l21 = set([s[1][0], s[1][1], s[1][2], s[1][3]])
        l22 = set([s[2][0], s[2][1], s[2][2], s[2][3]])
        l23 = set([s[3][0], s[3][1], s[3][2], s[3][3]])
        lx1 = set([s[0][0], s[1][1], s[2][2], s[3][3]])
        lx2 = set([s[0][3], s[1][2], s[2][1], s[3][0]])
        result = [l10 , l11 , l12 , l13 , l20 , l21 , l22 , l23 , lx1, lx2]
        #print result
        print "Case #" + str(i) + ":",
        if set(['O']) in result and (not set(['X']) in result) and (not set(['X', 'T']) in result):
            print "O won"
        elif set(['X']) in result and (not set(['O']) in result) and (not set(['O', 'T']) in result):
            print "X won"
        elif set(['O', 'T']) in result and (not set(['X']) in result) and (not set(['X', 'T']) in result):
            print "O won"
        elif set(['X', 'T']) in result and (not set(['O']) in result) and (not set(['O', 'T']) in result):
            print "X won"
        elif (set(['X']) in result or set(['X', 'T']) in result) and ((set(['O']) in result) or (set(['O', 'T']) in result)):
            print "Draw"
        elif not "." in l10.union(l11).union(l12).union(l13).union(l20).union(l21).union(l22).union(l23).union(lx1).union(lx2):
            print "Draw"
        else:
            print "Game has not completed"
        s = []
        i = i + 1

