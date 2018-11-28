#https://code.google.com/codejam/contest/3264486/dashboard#s=p1

flenames = ["test","B-small-attempt0","B-large"]  #.in for input .out for output
flemask = [0,0,1]   #toggle whether to run (1) or dont run (0) the filenames

def istidy(numin):
    numstr = str(numin)
    tidy = True
    idx = len(numstr) - 1
    while tidy and idx >= 1:
        if int(numstr[idx]) < int(numstr[idx - 1]):
            tidy = False
        else:
            idx -= 1

    return tidy, len(numstr) - idx


for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

#           inS, inK = [int(finp) for finp in flein.readline().split()]
            inN = int(flein.readline())

#            print 9999, istidy(9999)
#            print 100, istidy(100)
#            print 132, istidy(132)

            workN = inN
            isok, digit = istidy(workN)
#            print workN, isok, digit
            while not isok:
                factor = 10**digit
                workN = (workN / factor) * factor - 1
                isok, digit = istidy(workN)
#                print workN, isok, digit



            outpA = workN

            outstr = "Case #{}: {}".format(ctrL+1,outpA)

            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

