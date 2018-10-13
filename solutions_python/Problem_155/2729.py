# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:24:19 2015
"""

#read file
with open("A-large.in") as infile:
    firstline = infile.readline()
    f = open('A-large.out','a')
    for i, line in enumerate(infile):
        maxShyness, levels = line.strip().split()
        requiredPeople = 0
        standingPeople = 0
        for j in range(0, int(maxShyness) + 1):
            if j > standingPeople:
                requiredPeople +=1
                standingPeople += 1
            standingPeople += int(levels[j])

        #output      
        f.write("Case #"+str(i+1)+": "+str(requiredPeople)+"\n")
f.close()
