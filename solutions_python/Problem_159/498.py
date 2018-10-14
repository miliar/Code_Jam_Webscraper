#https://code.google.com/codejam/contest/6224486/dashboard

flenames = ["test","A-small-attempt0","A-large"]  #.in for input .out for output
flemask = [1,0,1]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inN = int(flein.readline())
            inM = [int(finp) for finp in flein.readline().split()]

            method1 = 0
            maxrate = 0
            for ctr in range(1,len(inM)):
                diff = -1 * min(inM[ctr] - inM[ctr-1],0)
                method1 += diff
                maxrate = max(maxrate,diff)

            method2 = 0
            for ctr in range(len(inM)-1):
                diff = min(inM[ctr],maxrate)
                method2 += diff

            outpA = str(method1) + " " + str(method2)

            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

