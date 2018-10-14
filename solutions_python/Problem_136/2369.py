#http://code.google.com/codejam/contest/2334486/dashboard#s=p1

flenames = ["test","B-small-attempt0","B-large"]  #.in for input .out for output
flemask = [1,0,1]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("F:\\Downloads\\CodeJam\\" + flenames[flectr] + ".in","r")
        fleout = file("F:\\Downloads\\CodeJam\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrT in range(inT):

            lnin = flein.readline().rstrip("\n").split()
            inC, inF, inX = [float(numin) for numin in lnin]

            prodrate = 2.0  #starting rate of 2.0 cookies per second
            tottime = 0.0   #time since start

            done = False
            while not done:
                ttc = inX / prodrate
                ttcalt = (inC / prodrate) + ((inX / (prodrate+inF)))
                if ttc <= ttcalt:                 #no more farms required
                    tottime += ttc
                    done = True
                else:
                    tottime += inC / prodrate   #time to get next farm
                    prodrate += inF              #new production rate



            outline = "{:.7}".format(tottime)

            outstr = "Case #{}: {}".format(ctrT+1,outline)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

