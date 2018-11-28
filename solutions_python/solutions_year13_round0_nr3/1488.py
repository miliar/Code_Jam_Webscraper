'''
Created on 13 mars 2013

@author: Steeve
'''

import sys
import math

def getPalUnder10(a, b):
    nb = 0
    if a <= 1 and 1 <= b:
        nb += 1
    if a <= 2 and 2 <= b:
        nb += 1
    if a <= 3 and 3 <= b:
        nb += 1
    return nb

def getPalStartsWith2(a, b):
    nb = 0
    i = 0
    while True:
        pal = long("2" + "0" * i + "2")
        if pal < a:
            i += 1
            continue
        if b < pal:
            break
        nb += 1
        i += 1
    return nb

def getPalStartsWith2_1inMiddle(a, b):
    nb = 0
    i = 0
    while True:
        pal = long("2" + "0" * i + "1" + "0" * i + "2")
        if pal < a:
            i += 1
            continue
        if b < pal:
            break
        nb += 1
        i += 1
    return nb

def getPalStartsWith1(a, b):
    nb = 0
    i = 0
    while True:
        pal = long("1" + "0" * i + "1")
        if pal < a:
            i += 1
            continue
        if b < pal:
            break
        nb += 1
        i += 1
    return nb

def getPalStartsWith1_2inMiddle(a, b):
    nb = 0
    i = 0
    while True:
        pal = long("1" + "0" * i + "2" + "0" * i + "1")
        if pal < a:
            i += 1
            continue
        if b < pal:
            break
        nb += 1
        i += 1
    return nb

def getPalStartsWith1_2inMiddle_1(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            if i + j > l:
                break
            pal = long("1" + "0" * i + "1" + "0" * j + "2" + "0" * j + "1" + "0" * i + "1")
            if a <= pal and pal <= b:
                nb +=1
    return nb

def getPalStartsWith1_by2(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            if i + j > l:
                break
            pal = long("1" + "0" * i + "1" + "0" * j + "0" * j + "1" + "0" * i + "1")
            if a <= pal and pal <= b:
                nb +=1
    return nb

def getPalStartsWith1_by3(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if i + j + k > l:
                    break
                pal = long("1" + "0" * i + "1" + "0" * j + "1" + "0" * k + "0" * k + "1" + "0" * j + "1" + "0" * i + "1")
                if a <= pal and pal <= b:
                    nb +=1
    return nb

def getPalStartsWith1_by4(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            for k in range(l):
                for m in range(l):
                    if i + j + k + m > l:
                        break
                    pal = long("1" + "0" * i + "1" + "0" * j + "1" + "0" * k + "1" + "0" * m + "0" * m + "1" + "0" * k + "1" + "0" * j + "1" + "0" * i + "1")
                    if a <= pal and pal <= b:
                        nb +=1
    return nb

def getPalStartsWith1_by2_1inMiddle(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            if i + j > l:
                break
            pal = long("1" + "0" * i + "1" + "0" * j + "1" + "0" * j + "1" + "0" * i + "1")
            if a <= pal and pal <= b:
                nb +=1
    return nb

def getPalStartsWith1_by3_1inMiddle(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if i + j + k > l:
                    break
                pal = long("1" + "0" * i + "1" + "0" * j + "1" + "0" * k + "1" + "0" * k + "1" + "0" * j + "1" + "0" * i + "1")
                if a <= pal and pal <= b:
                    nb +=1
    return nb

def getPalStartsWith1_by4_1inMiddle(a, b):
    nb = 0
    l = len(str(b))
    l = l / 2 + l % 2
    for i in range(l):
        for j in range(l):
            for k in range(l):
                for m in range(l):
                    if i + j + k + m > l:
                        break
                    pal = long("1" + "0" * i + "1" + "0" * j + "1" + "0" * k + "1" + "0" * m + "1" + "0" * m + "1" + "0" * k + "1" + "0" * j + "1" + "0" * i + "1")
                    if a <= pal and pal <= b:
                        nb +=1
    return nb

def getPalStartsWith1_1inMiddle(a, b):
    nb = 0
    i = 0
    while True:
        pal = long("1" + "0" * i + "1" + "0" * i + "1")
        if pal < a:
            i += 1
            continue
        if b < pal:
            break
        nb += 1
        i += 1
    return nb

def getPalAbove10(a, b):
    nb = 0
    nb += getPalStartsWith2(a, b)
    nb += getPalStartsWith2_1inMiddle(a, b)
    nb += getPalStartsWith1(a, b)
    nb += getPalStartsWith1_1inMiddle(a, b) 
    nb += getPalStartsWith1_2inMiddle(a, b)
    nb += getPalStartsWith1_2inMiddle_1(a,b)
    nb += getPalStartsWith1_by2(a,b)
    nb += getPalStartsWith1_by2_1inMiddle(a, b) 
    nb += getPalStartsWith1_by3(a, b)
    nb += getPalStartsWith1_by3_1inMiddle(a, b) 
    nb += getPalStartsWith1_by4(a ,b)
    nb += getPalStartsWith1_by4_1inMiddle(a, b) 
    return nb

def calcPal(a, b):
    nb = 0
    if b < 10:
        nb += getPalUnder10(a, b)
    elif a < 10:
        nb += getPalUnder10(a , 10)
        nb += getPalAbove10(10, b)
    else:
        nb += getPalAbove10(a, b)
    return nb

out_arr = []
filename = sys.argv[1]
with open(filename) as ifi:
    t = int(ifi.readline())
    for i in range(t):
        a , b = [long(n) for n in ifi.readline().split(" ")]
        print a, b
        answer = calcPal(long(math.ceil(math.sqrt(a))), long(math.floor(math.sqrt(b))))
        out_arr.append("Case #" + str(i + 1) + ": " + str(answer) + "\n")
ofilename = filename.split(".")[0] + ".out"
of = open(ofilename, "w")
of.writelines(out_arr)