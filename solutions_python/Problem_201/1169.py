#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Bilal Saim 2017 [Bilisel]
'''
import math
import sys
import os

def algorithm(num,inval):
    ##########################
    #Code Area
    n,k = inval.readline().strip().split()
    n = int(n)
    k = int(k)

    
    
    teks = 0
    cifts = 0
    tek = -1
    cift = -1
    if n % 2 == 1:
        teks = 1
        tek = n
    else:
        cifts = 1
        cift = n

    lrmin = 11
    lrmax = 11
    
##
##    if k>(int(n/4)*3):
##        lrmax = 0
##        lrmin = 0

    kademe = 1
    say = 0
    while True and lrmax != 0:
        #print("Case" +str(num+1) +"#Tek: " + str(tek) + " Teks: " + str(teks) + " Çift: " + str(cift) + " Çifts: " + str(cifts))
                                                                                       
        #print(str(num)+ " " + str(say))
        yteks = 0
        ycifts = 0
        ytek = -1
        ycift = -1
        if tek>=cift:
            if k<= say+teks:
                lrmin = int((tek-1)/2)
                lrmax = int((tek-1)/2)
                break
        elif cift>tek:
            if k<= say+cifts:
                lrmin = int((cift)/2 -1)
                lrmax = int((cift)/2)
                break
        if k<= say+teks+cifts:
            if tek<cift:
                lrmin = int((tek-1)/2)
                lrmax = int((tek-1)/2)
            else:
                lrmin = int((cift)/2 -1)
                lrmax = int((cift)/2)
            break
        
        say += (teks+cifts)

        ateks = 0
        acifts = 0
        if cifts != 0:
            ateks = cifts
            acifts = cifts
            deg = int(cift/2)
            if deg % 2 == 0:
                ycift = deg
                ytek = deg-1
            else:
                ycift = deg -1
                ytek = deg
            
        if teks != 0:
            if int((tek-1)/2) % 2 == 0:
                ycifts = teks*2 + acifts
                yteks = ateks
                ycift = int((tek-1)/2)
            else:
                yteks = ateks + teks*2
                ytek = int((tek-1)/2)
                ycifts = acifts
        else:
            ycifts = acifts
            yteks = ateks

        cifts = ycifts
        teks = yteks
        tek = ytek
        cift = ycift
        
        if ycifts == 0:
            cifts = 0
        if yteks == 0:
            teks = 0

##    dizi = []
##
##    if n % 2 == 1:
##        dizi.append(int((n-1)/2))
##        dizi.append(int((n-1)/2))
##    else:
##        dizi.append(int((n)/2-1))
##        dizi.append(int((n)/2))
##
##    lrmax = dizi[1]
##    lrmin = dizi[0]
##        
##    if k>(int(n/4)*3):
##        lrmax = 0
##        lrmin = 0
##        
##    say = 1
##    if lrmax == 0:
##        aaa = 0
##    else:
##        while True and k != 1 and lrmax != 0:
##            mval = max(dizi)
##            ind = dizi.index(mval)
##
##            if mval % 2 == 1:
##                yeni = [int(mval/2)]*2
##            else:
##                yeni = [int(mval/2-1),int(mval/2)]
##
##            dizi = dizi[:ind] + yeni + dizi[ind+1:]
##            say += 1
##            if k == say or mval == 1:
##                lrmin = yeni[0]
##                lrmax = yeni[1]
##                break
            
    result = str(lrmax) + " " + str(lrmin)
    
    #
    ##########################
    return "Case #"+ str(num+1) +": " + result + "\n"


##########################
#CODES FOR LAZYJAM
##########################
text = ""
data = "test"
infile = "Input-test.txt"
print("Running...")
if os.path.isfile("Operation.txt"):
    with open("Operation.txt","r") as t:
        data = t.readline().strip()
        infile = t.readline().strip()

#We read input values from file
inval = open(infile,"r")

#If there is limit for case!
tnumber = int(inval.readline().strip())
    
for num in range(0,tnumber):
    text += algorithm(num,inval)

dosya = open("Output-"+data+".txt", "w")
dosya.write(text)
dosya.close()

print("Output:")
print(text)

#print(text)
if data == "test":
    with open("Output.txt") as t:
        a = t.readlines()
    with open("Output-test.txt") as t:
        b = t.readlines()

    if a==b:
        print("Results are smiliar")
    else:
        print("Results didn't match!")
