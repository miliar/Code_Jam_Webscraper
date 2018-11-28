#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    testcases = int(input())
     
    for caseNr in range(1, testcases+1):
        cipher = input()

        splitArray = cipher.split()
        smax = int(splitArray[0])
        visitors = []
        for j in range(0, smax + 1):
        	visitorsMas = splitArray[1]
        	visitors.append(int(splitArray[1][j]))
        
        invite = 0
        alreadyGetUp = 0
        for i in range(0, smax+1):
            if visitors[i] != 0:
                if i > alreadyGetUp:
                    invite += i - alreadyGetUp
                    alreadyGetUp += invite

                alreadyGetUp += visitors[i]

        print("Case #%i: %s" % (caseNr, str(invite)))