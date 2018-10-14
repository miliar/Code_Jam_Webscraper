#!/usr/bin/python2.7
#
# Code Jam 2011
# 7 May 2011 - Qualification
#
# B - Magicka
#
# Copyright (c) 2011 efoftee
#
# This program or module is free software is licensed under a
# Creative Commons Attribution-Noncommercial-Share Alike 3.0 Unported License
# See http://creativecommons.org/licenses/by-nc-sa/3.0/ for details
#


##Input 
##
##5
##0 0 2 EA
##1 QRI 0 4 RRQR
##1 QFT 1 QF 7 FAQFDFQ
##1 EEZ 1 QE 7 QEEEERA
##0 1 QW 2 QW
##
##Output
##
##Case #1: [E, A]
##Case #2: [R, I, R]
##Case #3: [F, D, T]
##Case #4: [Z, E, R, A]
##Case #5: []


import sys
from itertools import tee, izip, islice

inp, out = sys.stdin, sys.stdout

def log(case, output):
    result = "Case #%d: [" %case
    s = None
    for s in output:
        result += s
        result += ", "

    if s:
        out.write(result[:-2])
    else:
        out.write(result)
    out.write("]\n")
    out.flush()


def invoke(s, combines, opposes):
    for c in combines:
        if s[-2:] == c[:-1] or s[-2:] == c[:-1][::-1]:
            s = s[:-2] + c[-1]
            
    for op in opposes:
        if s.count(op[0]) and s.count(op[1]):
            s = ''

    return s


def test():
    T = int(inp.readline())
    
    for case, line in enumerate(inp.readlines(), 1):
        nline = line.rstrip('\n').split(' ')
        C = int(nline[0])
        combines = nline[1:C+1]
        D = int(nline[C+1])
        opposes = nline[C+2:C+1+D+1]
        #N = int(nline[C+1+D+1])
        girdi = nline[-1]
        
        news = ''        
        for char in girdi:            
            news = invoke(news+char, combines, opposes)            
            
        log(case, news)
        

if __name__ == '__main__':    
    test()
