#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'dshgna'


def readAns(ans):
    linec = 1
    res = []
    while(linec <= 4):
        if (linec == ans):
            res = [int(x) for x in f.readline().split()]
        else:
            f.readline()
        linec = linec + 1
    return res


def solve(r1, r2):
    s1 = sorted(r1)
    s2 = sorted(r2)
    count = 0
    guess = 0
    for x in s1:
        for y in s2:
            if (x == y):
                count = count + 1
                guess = x
            elif (x > y):
                continue
    if (count == 0):
        return "Volunteer cheated!"
    elif (count == 1):
        return guess
    else:
        return "Bad magician!"

if __name__ == "__main__":
    f = file("A-small-attempt0.in")
    fout = file("output.txt", "w+")
    T = int(f.readline())
    #print "Test Cases: ", T
    for case in range(1, T+1):
        ans1 = int(f.readline())
        #print ans1
        res1 = readAns(ans1)
        #print res1
        ans2 = int(f.readline())
        #print ans2
        res2 = readAns(ans2)
        #print res2
        sol = solve(res1, res2)
        out = "Case #%s: %s \n" % (case, sol)
        print out
        fout.write(out)

    fout.close()
    f.close()