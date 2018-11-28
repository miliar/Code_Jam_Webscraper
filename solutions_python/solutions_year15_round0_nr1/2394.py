#!/usr/bin/python3
#coding: utf-8
#from numpy import *

def nfriends(input_string):
    ssplit = input_string.split()
    npeople = int(ssplit[0])
    shyLvls = list(map(int, list(ssplit[1])))
    standing = 0
    nfriends = 0
    for i, lvl in enumerate(shyLvls):
        stoodUp = False
        while not stoodUp:
            if standing >= i:
                standing += lvl
                stoodUp = True
            else:
                standing += 1
                nfriends += 1
    return nfriends


def process_input(filename):
    with open(filename, "r") as f:
        ncases = int(f.readline())
        i = 1
        for line in f:
            print("Case #{0}: {1}".format(i, nfriends(line)))
            i += 1

import sys
try:
    process_input(sys.argv[1])
except:
    print("no input")


