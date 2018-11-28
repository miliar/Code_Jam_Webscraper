#!/usr/bin/python

import copy

try:
        with open("B-small-attempt0.in") as inFile, open("output.txt", "w") as outFile:
                cases = int(inFile.readline().strip())
                for c in range(cases):
                        outFile.write("Case #" + str(c+1) + ": ")
                        area = inFile.readline().split(" ")
                        N = int(area[0])
                        M = int(area[1])
                        grid = []
                        
                        for each in range(N):
                                row = inFile.readline().strip().split(" ")
                                grid.append(row)
                        strOut = ""
                        while strOut == "":
                                for row in grid:
                                        grow = copy.copy(row)
                                        grow.sort()
                                        if grow[0] != grow[len(grow)-1]:
                                                for c in range(M):
                                                        if row[c] != grow[len(grow)-1]:
                                                                cuttable = True
                                                                while cuttable == True:
                                                                        for r in range(N):
                                                                                if grid[r][c] > row[c]:
                                                                                        cuttable = False
                                                                                        break;
                                                                        break;
                                                                if cuttable == False:
                                                                        strOut = "NO\n"
                                break;
                        if strOut == "":
                                outFile.write("YES\n")
                        else:
                                outFile.write(strOut)
  
except IOError as err:
        print(str(err))
