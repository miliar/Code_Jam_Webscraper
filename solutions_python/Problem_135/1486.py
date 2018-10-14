#!usr/bin/python

import sys

with open(sys.argv[1],"r") as inf:
    with open(sys.argv[2],"w") as outf:
        if inf and outf:
            T = int(inf.readline().strip()) # num of cases

            def getChoices(arr):
                picks = int(inf.readline().strip())
                for n in range(1,5):
                    line = inf.readline()
                    if n is picks:
                        arr = line.strip().split(" ")
                return arr

            for t in range(1,T+1):
                firChoices = getChoices([])
                secChoices = getChoices([])
                
                pick = 0
                match = 0
                for n in firChoices:
                    if n in secChoices:
                        match+=1
                        pick = n

                if match is 0:
                    outf.write("Case #" + str(t) + ": Volunteer cheated!\n")
                elif match is 1:
                    outf.write("Case #" + str(t) + ": " + str(pick) + "\n")
                else:
                    outf.write("Case #" + str(t) + ": Bad magician!\n")

            #end for
        #end inf and outf
    #end open outf
#end open inf







            


        
    
