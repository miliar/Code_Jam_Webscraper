import sys

if __name__ == "__main__":

    f = open(sys.argv[1])
    lines = f.readlines()
    cases = int(lines[0])

    for line in range(1, cases + 1):
        print "Case #%d:" % (line),
        totalp = []
        phrase = lines[line].split()
        googlers = int(phrase[0])
        surprising = int(phrase[1])
        best = int(phrase[2])
        for i in range(3, googlers + 3):
            totalp.append(int(phrase[i]))
        totalp = sorted(totalp)
        mod0 = []
        mod1 = []
        mod2 = []
        for score in totalp:
            if (score % 3 == 0):
                mod0.append(score)
            elif (score % 3 == 1):
                mod1.append(score)
            else:
                mod2.append(score)

        #print "############################"
        #print "Mod3_0 = ", mod0
        #print "Mod3_1 = ", mod1
        #print "Mod3_2 = ", mod2

        matches = []

        #print "Surprising = ", surprising

        for score0 in mod0:
            if (best == 0):
                matches.append(score0)
            elif (score0):
                if (score0 >= 3 * best):
                    matches.append(score0)
                elif (score0 % best == best - 3) and (score0 > 2 * best):
                    if surprising:
                        matches.append(score0)
                        surprising -= 1


        #print "Surprising = ", surprising

        for score1 in mod1:
            if best == 0:
                matches.append(score1)
            elif (score1 >= 3 * best):
                matches.append(score1)
            elif (score1 % best == best - 2) and (score1 > 2 * best):
                matches.append(score1)


        #print "Surprising = ", surprising

        for score2 in mod2:
            if best == 0:
                matches.append(score2)
            elif (score2 >= 3 * best) or (3 * best - 1 == score2):
                matches.append(score2)
            elif (score2 % best <= best - 4) and (score2 > 2 * best):
                if surprising:
                    matches.append(score2)
                    surprising -= 1
        print len(matches)
        #print "Matches = ", matches
        #print "############################\n"
