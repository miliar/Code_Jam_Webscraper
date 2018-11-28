#http://code.google.com/codejam/contest/2334486/dashboard#s=p1

flenames = ["test","A-small-attempt0","B-large-practice"]  #.in for input .out for output
flemask = [1,1,0]   #toggle whether to run (1) or dont run (0) the filenames

for flectr in range(3):
    if flemask[flectr] == 1:
        print "Running test file: {}".format(flenames[flectr])

        flein = file("F:\\Documents\\Documents\\Python\\CodeJam\\2014\\" + flenames[flectr] + ".in","r")
        fleout = file("F:\\Documents\\Documents\\Python\\CodeJam\\2014\\" + flenames[flectr] + ".out","w")

        inT = int(flein.readline())

        for ctrT in range(inT):
            ans1 = int(flein.readline())
            grid = []
            for ctr in range(4):
                lnin = flein.readline().rstrip("\n").split()
                thisrow = [int(numin) for numin in lnin]
                grid.append(thisrow)
            possans1 = grid[ans1-1]

            ans2 = int(flein.readline())
            grid = []
            for ctr in range(4):
                lnin = flein.readline().rstrip("\n").split()
                thisrow = [int(numin) for numin in lnin]
                grid.append(thisrow)
            possans2 = grid[ans2-1]

            ans = []

            for ctrP in range(4):
                if possans1[ctrP] in possans2:
                    ans.append(possans1[ctrP])

            if len(ans) == 1:
                outline = ans[0]
            elif len(ans) == 0:
                outline = "Volunteer cheated!"
            else:
                outline = "Bad magician!"

            outstr = "Case #{}: {}".format(ctrT+1,outline)
            print outstr
            fleout.write(outstr + "\n")


        flein.close()
        fleout.close()

