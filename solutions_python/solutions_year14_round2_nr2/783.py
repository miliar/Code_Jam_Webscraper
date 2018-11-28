
# ----------------------------------------------
# Booz
# May 3, 2014
# 2014 Code Jam 
# Round 1B
# Problem B - New Lottery Game
# ----------------------------------------------

from datetime import datetime
import itertools

def getNums(indat):
    return indat[0] & indat[1]

if __name__ == "__main__":
    SMALL   = 0
    LARGE   = 1
    TEST    = 2
    DATASET = SMALL

    fins  = ["round_1b\\b\\1b_b_s.in",  "round_1b\\b\\1b_b_l.in" , "round_1b\\b\\test.in" ]
    fouts = ["round_1b\\b\\1b_b_s.out", "round_1b\\b\\1b_b_l.out", "round_1b\\b\\test.out"]

    st = datetime.now()

    inf = open(fins[DATASET], "r")
    outf = open(fouts[DATASET], "w")

    test_cases = int(inf.readline())
    for tc in range(test_cases):
        indat  = map(int, inf.readline().split())
        a      = indat[0]
        b      = indat[1]
        k      = indat[2]
        combos = map(getNums, itertools.product([i for i in range(a)], [j for j in range(b)]))
        wrtdat = len([i for i in combos if i < k])

    	outf.write("Case #%d: %d\n" % ((tc+1), wrtdat))

    inf.close()
    outf.close()

    print "Answer in: " + str(datetime.now() - st)
