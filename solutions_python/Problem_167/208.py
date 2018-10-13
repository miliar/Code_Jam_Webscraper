#https://code.google.com/codejam/contest/4244486/dashboard

flenames = ["testC","C-small-attempt0","C-large"]  #.in for input .out for output
flemask = [1,1,0]   #toggle whether to run (1) or dont run (0) the filenames

def fillin(startF, denomsF):
    times = 0
    ctrF = startF
    while ctrF <= inV and times <= inC:
        check[ctrF] = 1
        if len(denomsF) > 1:
            fillin(ctrF, denomsF[1:])
        ctrF += denomsF[0]
        times += 1



for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inC, inD, inV = [int(finp) for finp in flein.readline().split()]
            denoms = [int(finp) for finp in flein.readline().split()]
            denoms.reverse()

            check = [0] * (inV+1)
            check[0] = 1    #0

            fillin(0, denoms)

            new = 0
            while check.count(0) > 0:
                new += 1
                first = check.index(0)
                denoms.append(first)
                denoms.sort(reverse=True)
                fillin(0,denoms)

            outpA = new

            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

