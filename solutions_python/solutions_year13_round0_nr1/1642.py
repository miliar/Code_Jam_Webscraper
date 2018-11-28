#!/usr/bin/python

import copy

def fullRow(grow):
        retStr = ""
        if not "." in grow:
                if not "T" in grow:
                        if grow[0] == grow[1] and grow[0]== grow[2] and grow[0] == grow[3]:
                                retStr = grow[0] + " won\n"
                                return retStr;
                else:
                        brow = copy.copy(grow)
                        brow.sort()
                        if brow[0] == "T" or brow[3] == "T":
                                retStr = brow[1] + " won\n"
                                return retStr;
        return retStr;

try:
        with open("A-large.in") as inFile, open("output.txt", "w") as outFile:
                cases = int(inFile.readline().strip())
                for c in range(cases):
                        winner = ""
                        outFile.write("Case #" + str(c+1) + ": ")
                        grid = []
                        for a in range(4):
                                line = inFile.readline().strip()
                                row = [line[0].strip(), line[1].strip(), line[2].strip(), line[3].strip()]
                                grid.append(row)
                        if winner == "":
                                for row in grid:
                                        winner = fullRow(row)
                                        if winner != "":
                                                break;
                        if winner == "":
                                for number in range(4):
                                        winner = fullRow([grid[0][number], grid[1][number], grid[2][number], grid[3][number]])
                                        if winner != "":
                                                break;
                        if winner == "":
                                winner = fullRow([grid[0][0], grid[1][1], grid[2][2], grid[3][3]])
                        if winner == "":
                                winner = fullRow([grid[0][3], grid[1][2], grid[2][1], grid[3][0]])
                        if winner == "":
                                if "." in grid[0] or "." in grid[1] or "." in grid[2] or "." in grid[3]:
                                        winner = "Game has not completed\n"
                                else:
                                        winner = "Draw\n"
                        outFile.write(winner)
                        trash = inFile.readline()
except IOError as err:
        print(str(err))
