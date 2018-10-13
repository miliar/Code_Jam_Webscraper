#https://code.google.com/codejam/contest/6224486/dashboard

flenames = ["test","D-small-attempt0","D-large-attempt0"]  #.in for input .out for output
flemask = [1,1,0]   #toggle whether to run (1) or dont run (0) the filenames

numShapes = [0,1,1,2,5]
minDim = [0,1,1,2,3]

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("f:\\live\\downloads\\" + flenames[flectr] + ".in","r")
        fleout = file("f:\\live\downloads\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrL in range(inT):

            inX, inR, inC = [int(finp) for finp in flein.readline().split()]

            if ((inR * inC) % inX != 0) or (min(inC,inR) < minDim[inX]):
                outpA = "RICHARD"
            else:
                outpA = "GABRIEL"

            outstr = "Case #{}: {}".format(ctrL+1,outpA)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

