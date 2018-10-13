#!/usr/bin/env python

import math
import sys


def main():
    argv = sys.argv
    if len(argv)>1:
        inFile = argv[1]
    else:
        directory = "/home/sedwardsparton/Downloads/"
        inFile=directory+"A-small.in"
    
    outfile = "codeJam.out"
    
    input = open(inFile)
    output = open(outfile, "w")
    
    line = input.readline().strip()
    cases = int(line)
    
    for case in range (0, cases):
        line = input.readline().strip()
        noTeams = int(line)
        results = []
        WP = []    
        OWP = []
        
        for i in range(0,noTeams):
            stringResults = line = input.readline().strip()
            indResults = []
            won =0
            lost = 0
            for j in range(0, noTeams):
                res = stringResults[j]
                if res == '1':
                    won += 1.0
                    indResults.append(1)
                elif res == '0':
                    indResults.append(-1)
                    lost+=1.0
                else:
                    indResults.append(0)
            results.append(indResults)
            WP.append(won/(won+lost))
            
            OWPSum = 0
            tmpOWP = []
            for j in range(0, noTeams):
                if indResults[j]==1:
                    val = (won-1)/(won+lost-1)
                elif indResults[j]==-1:
                    val = (won)/(won+lost-1)
                else:
                    val = (won)/(won+lost)
                
                tmpOWP.append(val)
                
            OWP.append(tmpOWP)
                    
        print >> output, "Case #%d:" % (case+1)
        print "Case #%d" % (case+1)

        OWPArray = []
        for i in range(0,noTeams):
            played = 0
            valOWP = 0
            for j in range(0, noTeams):
                if abs(results[i][j])>0:
                    valOWP += OWP[j][i]
                    played+=1
            OWPArray.append(valOWP/played)
            
        for i in range(0,noTeams):
            played = 0
            valOOWP = 0
            valOWP = OWPArray[i]
            for j in range(0, noTeams):
                if abs(results[i][j])>0:
                    valOOWP += OWPArray[j]
                    played+=1
            
            
            outputdata = 0.25 * (WP[i]) + 0.50 * (valOWP) + 0.25 * (valOOWP/played)
            print >> output, outputdata


if __name__ == '__main__':
	main()
