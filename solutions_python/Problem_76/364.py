# -*- coding: utf-8 -*-
from __future__ import with_statement

import sys
from itertools import *

def len_bin(x):
    if x//2==0:
        return 1
    return 1 + len_bin(x//2)

def get_c(list, index):
    if index>len(list)-1:
        return 0
    return list[index]

def add_bin(a, b):
    al=[a>>i&1 for i in range(0, len_bin(a))] 
    bl=[b>>i&1 for i in range(0, len_bin(b))] 

    c = len(al)
    if len(bl)>c:
        c=len(bl)

    rb=[]
    for i in range(0, c):
        rb.append(get_c(al,i)^get_c(bl,i))

    ri = 0
    for i,b in enumerate(rb):
        ri += 2**(i)*b

    return ri

def add_bin_list(nums):
    sum=0
    for num in nums:
        sum = add_bin(sum, num) 
    return sum

def to_result(keep):
    if keep<0:
        return "NO"
    return str(keep)

if len(sys.argv) < 2:
    print "error"
    sys.exit()

infile = sys.argv[1]
outfile = "outc"

with open(infile, "r") as f:
    lines = f.read().splitlines()
    
T = int(lines[0])

outlines=[]
for num in range(0, T):
    num_of_candies = int(lines[num*2+1])
    piece_list = [int(i) for i in lines[num*2+2].split(" ")]

    piece_list.sort()

    c=len(piece_list)
    keep=-1
    for i in range(0, c):
        a1=islice(piece_list, 0, i+1)
        a2=islice(piece_list, i+1, c)
        a1sum=add_bin_list(a1)
        a2sum=add_bin_list(a2)
        if a1sum==a2sum:
            a2=islice(piece_list, i+1, c)
            keep=sum(a2)
            break

    outlines.append("Case #%d: %s" %(num+1, to_result(keep)))

with open(outfile, "w") as f:
    for line in outlines:
        f.write(line + "\n")


