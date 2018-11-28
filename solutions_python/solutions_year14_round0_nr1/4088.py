# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 00:44:12 2014

@author: jessicahoffmann
"""

import sys

def main():
    mon_fichier = open("trick.txt", "w")
    mon_fichier.seek(0)
    n = int(sys.stdin.readline())
    for j in range(n):
        nIntersections = 0
        goodNumber = 0
        mon_fichier.write("Case #")
        mon_fichier.write(str(j+1))
        mon_fichier.write(": ")
        nLine = int(sys.stdin.readline())
        for i in range(4):
            if i==nLine-1:
                l1 = map(int,sys.stdin.readline().split())
            else :
                sys.stdin.readline()
        
        nLine = int(sys.stdin.readline())
        for i in range(4):
            if i==nLine-1:
                l2 = map(int,sys.stdin.readline().split())
            else :
                sys.stdin.readline()
                    
        for elt1 in l1:
            for elt2 in l2:
                if elt1==elt2:
                    nIntersections += 1
                    goodNumber = elt1
                    
        if nIntersections == 0:
            mon_fichier.write("Volunteer cheated!\n")
        if nIntersections == 1:
            mon_fichier.write(str(goodNumber) + "\n") 
        if nIntersections >= 2:
            mon_fichier.write("Bad magician!\n")
    mon_fichier.close()
            
main()