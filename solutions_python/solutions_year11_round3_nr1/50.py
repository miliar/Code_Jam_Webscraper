#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# Input
  	
# Output
 
# 3
# 2 3
# ###
# ###
# 1 1
# .
# 4 5
# .##..
# .####
# .####
# .##.. 	Case #1:
# Impossible
# Case #2:
# .
# Case #3:
# ./\..
# .\//\
# ./\\/
# .\/.. 
f = open(sys.argv[1])
nb_case = int(f.readline())
for i in range(nb_case):
    print("Case #" + str(i+1) + ":")
    response = 0
    psize = f.readline()[:-1].split(" ")
    nb_line = int(psize[0])
    tableau = []
    nb_blue = 0
    for j in range(nb_line):
        tableau.append(f.readline()[:-1])
        nb_blue += tableau[j].count("#")
    if nb_blue%4 != 0:
        print("Impossible")
        continue
    if nb_blue == 0:
        for t in tableau:
            print(t)
        continue
    
    impossible = 0
    tab = []
    for t in tableau:
        if t.count("#") % 2 != 0:
            impossible = 1
            break
        tab.append(list(t))
    if impossible == 1:
        print("Impossible")
        continue        

    for j,t in enumerate(tab):
        for k, c in enumerate(t):
            if c == '#':
                if t[k+1] != '#' or j+1 == len(tab) or tab[j+1][k] != '#' or tab[j+1][k+1] != "#":
                    print("Impossible")
                    impossible = 1
                    break
                t[k] = "/"
                t[k+1] = "\\"
                tab[j+1][k] = "\\"
                tab[j+1][k+1] = "/"
        if impossible == 1:
            break
    if impossible == 1:
        continue
    for t in tab:
        for c in t:
            sys.stdout.write(c)
        sys.stdout.write("\n")


    
