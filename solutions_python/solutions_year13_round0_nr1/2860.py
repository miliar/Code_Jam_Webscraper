#!/usr/bin/python

import sys

def posT(mp):
    k = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if mp[i][j] != ".":
                k += 1
    if k == 4 * 4:
        return 1
    return 0
pass

def result(mp):
    k = 0
    i = 0
    for i in range(0, 4):
        g = mp[i][0]
        if g == "T":
            g = mp[i][1]
        j = 0
        for j in range(0, 4):
            if g == mp[i][j] or mp[i][j] == "T":
                k += 1
        if k == 4 and g != ".":
            return g + " won"
        else:
            k = 0
    j = 0
    k = 0
    for j in range(0, 4):
        g = mp[0][j]
        if g == "T":
            g = mp[1][0]
        i = 0
        for i in range(0, 4):
            if g == mp[i][j] or mp[i][j] == "T":
                k += 1
        if k == 4 and g != ".":
            return g + " won"
        else:
            k = 0
    k = 0
    i = 0
    g = mp[i][i]
    if g == "T":
        g = mp[i+1][i+1]
    for i in range(0, 4):
        if g == mp[i][i] or mp[i][i] == "T":
            k+=1
    if k == 4 and g != ".":
        return g + " won"
    i = 3
    j = 0
    k = 0
    g = mp[0][3]
    if g == "T":
        g = mp[i-3][i-1]
    while i >= 0:
        if g == mp[i][j] or mp[i][j] == "T":
            k+=1
        i-=1
        j+=1
    if k == 4 and g != ".":
        return g + " won"
    if posT(mp) == 0:
        return "Game has not completed"
    return "Draw"
pass

def output(lines):
    mp = [["","","",""],["","","",""],["","","",""],["","","",""]]
    i = 0
    for line in lines:
        j = 0
        for c in list(line):
            mp[i][j] = c
            j+=1
            if j == 4:
                break
        i+=1
    return result(mp)
pass

def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        src = open(filename, "r")
        lines = src.readlines()
        src.close()
        n = int(lines[0])
        if n < 1 or n > 10:
            return
        j = 1
        outfile = open(filename.split(".")[0] + ".out", "w")
        for i in range(0, n):
            print("Case #" + str(i + 1) + ": " + str(output(lines[j:j+4])))
            outfile.write("Case #" + str(i + 1) + ": " + str(output(lines[j:j+4])))
            if i != n-1:
                outfile.write("\n")
            j += 1 + 4
pass

if __name__ == "__main__":
    main()
