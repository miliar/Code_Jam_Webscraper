#https://code.google.com/codejam/contest/4244486/dashboard

flenames = ["test","A-small-attempt2","A-large"]  #.in for input .out for output
flemask = [1,1,0]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\codejam\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\codejam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inR, inC, inW = [int(finp) for finp in flein.readline().split()]

#           inp = flein.readline().split()

#           total = inC - (inC - inW) // inW * (inW - 1)

            total = 0
            rest = inC
            while rest > inW:
                total += 1   #guess
                rest = max(rest - inW, inW)
            total += rest
            total *= inR


            outpA = total

            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr, inR, inC, inW
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

