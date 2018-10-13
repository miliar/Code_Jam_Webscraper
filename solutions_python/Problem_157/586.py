import sys

fin = open(sys.argv[1], 'r')

cases = int(fin.readline())

def str_to_q(c):
    if c == 'i':
        return 0, 1, 0, 0
    elif c == 'j':
        return 0, 0, 1, 0
    else:
        return 0, 0, 0, 1

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

def out(c, bool):
    if bool:
        w = "YES"
    else:
        w = "NO"
    print "Case #%d: %s" % (c, w)

for case in range(1, cases+1):
    _, p = map(int, fin.readline().split())
    qstr = fin.readline().strip()
    letters = []
    quickTest = 1, 0, 0, 0
    foundI = foundJ = foundK = False
    i = str_to_q('i')
    j = str_to_q('j')
    k = str_to_q('k')
    for c in qstr:
        q = str_to_q(c)
        letters.append(q)
        quickTest = q_mult(quickTest, q)
        if q == i:
            foundI = True
        elif q == j:
            foundJ = True
        else:
            foundK = True

    if not (foundI and foundK or foundI and foundJ or foundK and foundJ):
        out(case, False)
        continue

    foundI = foundJ = foundK = False

    sp = p % 4
    #print "puissance", sp
    #print "quickTest", quickTest
    quickTestBis = quickTest
    for g in range(1, sp):
        quickTest = q_mult(quickTest, quickTestBis)
        #print "quickTestBis^%d" % (g+1), quickTestBis

    #print "quickTest: ", quickTest

    if quickTest == (-1, 0, 0, 0):
        new = True
        for ip in range(0, min(100,p)):
            for q in letters:
                if new:
                    q1 = q
                    new = False
                else:
                    q2 = q
                    q1 = q_mult(q1, q2)

                #print q1
                if not foundI and q1 == i:
                    foundI = True
                    new = True
                    #print "found I"
                elif foundI and not foundJ and q1 == j:
                    foundJ = True
                    #print "found J"
                    new = True
                elif foundI and foundJ and q1 == k:
                    #print "found K"
                    foundK = True
                    break
            if foundK:
                break

        out(case, foundK)
    else:
        out(case, False)




