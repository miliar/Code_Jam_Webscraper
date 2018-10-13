#!/usr/bin/python

import sys

inputfile = open(sys.argv[1], 'r').read().split('\n')
outputfile = open("./output.2", 'w')

numcases = int(inputfile[0])
currcase = 0
totallines = 1

while currcase < numcases:
        adepartlist, aarrivelist, bdepartlist, barrivelist = [], [], [], []
        turnaround = int(inputfile[totallines])
        totallines += 1
        bystation = inputfile[totallines].split(' ')
        atimes = int(bystation[0])
        btimes = int(bystation[1])
        totallines += 1

        currtime = 0
        while currtime < atimes:
                schedule = inputfile[totallines + currtime].split(' ')
                departure = schedule[0].split(':')
                arrival = schedule[1].split(':')
                departtime = 60*int(departure[0]) + int(departure[1])
                arrivetime = 60*int(arrival[0]) + int(arrival[1]) + turnaround
                adepartlist += [departtime]
                aarrivelist += [arrivetime]
                currtime += 1
        totallines += atimes

        currtime = 0
        while currtime < btimes:
                schedule = inputfile[totallines + currtime].split(' ')
                departure = schedule[0].split(':')
                arrival = schedule[1].split(':')
                departtime = 60*int(departure[0]) + int(departure[1])
                arrivetime = 60*int(arrival[0]) + int(arrival[1]) + turnaround
                bdepartlist += [departtime]
                barrivelist += [arrivetime]
                currtime += 1
        totallines += btimes

        ## A TO B
        aarrivelist.sort()
        bdepartlist.sort()

        aindex, bindex = 0, 0
	abmatches = 0
        while aindex < len(aarrivelist) and bindex < len(barrivelist):
                if aarrivelist[aindex] <= bdepartlist[bindex]:
                        aindex += 1
                        bindex += 1
                        abmatches += 1
                else:
                        bindex += 1

        numbtrains = btimes - abmatches

        ## B TO A
        barrivelist.sort()
        adepartlist.sort()

        aindex, bindex = 0, 0
        bamatches = 0
        while aindex < len(aarrivelist) and bindex < len(barrivelist):
                if barrivelist[bindex] <= adepartlist[aindex]:
                        aindex += 1
                        bindex += 1
                        bamatches += 1
                else:
                        aindex += 1
	
        numatrains = atimes - bamatches

        currcase += 1
        outputfile.write("Case #" + str(currcase) + ": " + str(numatrains) + " " + str(numbtrains) + "\n")