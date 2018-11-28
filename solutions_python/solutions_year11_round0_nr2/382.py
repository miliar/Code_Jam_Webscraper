# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys


class Combination():
    elements=[]
    combine=""

    def __init__(self, s):
        if len(s)<3:
            return
        self.elements=[item for i, item in enumerate(s) if i<2]
        self.elements.sort()
        self.combine=s[2]

class Opposed():
    elements=[]
    def __init__(self, s):
        if len(s)<2:
            return
        self.elements=[item for i, item in enumerate(s) if i<2]
        self.elements.sort()

def do_combine(element_list, combination_list):
    if len(combination_list)==0:
        return False
    if len(element_list)<2:
        return False

    c=len(element_list)
    s=[element_list[c-2], element_list[c-1]]
    s.sort()

    for combination in combination_list:
        if s==combination.elements:
            element_list.pop()
            element_list.pop()
            element_list.append(combination.combine)
            return True 
    return False

def is_start(c, opposed):
    if c==opposed.elements[0]:
        return 0
    if c==opposed.elements[1]:
        return 1
    return -1

def is_opposed(c, opposed, index):
    if c==opposed.elements[1-index]:
        return True
    return False

def do_opposed(element_list, opposed_list):
    if len(opposed_list)==0:
        return
    if len(element_list)<2:
        return
    i=0
    for opposed in opposed_list:
        c = len(element_list)
        for i in range(0, c):
            index=is_start(element_list[i], opposed)
            if index == -1:
                continue
            if is_opposed(element_list[c-1], opposed, index):
                for n in range(0,c):
                    element_list.pop()
                return
    
def to_result_string(items):
    return "[" + ", ".join(items) + "]"


if len(sys.argv) < 2:
    print "error"
    sys.exit()

infile = sys.argv[1]
outfile = "outb"

with open(infile, "r") as f:
    lines = f.read().splitlines()
    
T = int(lines[0])

outlines=[]
for num in range(1, T+1):
    ss = lines[num].split(" ")

    i=0
    combination_list = [Combination(ss[i+1+j]) for j in range(0, int(ss[i]))]
    i+=int(ss[i])
    i+=1
    opposed_list = [Opposed(ss[i+1+j]) for j in range(0, int(ss[i]))]
    i+=int(ss[i])
    i+=1
    invoke_list = [item for j,item in enumerate(ss[i+1]) if i<ss[i]]
    i+=int(ss[i])
    
    #print
    #print "combination_list=",combination_list
    #print "opposed_list=", opposed_list
    #print "invoke_list=", invoke_list
    #for o in combination_list:
    #    print "combination_list", o.elements
    #for o in opposed_list:
    #    print "opposed_list", o.elements
    #print "invoke_list=", invoke_list

    element_list=[]
    for invoke in invoke_list:
        element_list.append(invoke)
        if do_combine(element_list, combination_list)==False:
            do_opposed(element_list, opposed_list)

    outlines.append("Case #%d: %s" %(num, to_result_string(element_list)))


with open(outfile, "w") as f:
    for line in outlines:
        f.write(line + "\n")


