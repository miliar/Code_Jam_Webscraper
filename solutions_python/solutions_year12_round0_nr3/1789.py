#!/usr/bin/python
import os
import sys
import string
from collections import deque

ifile = open(sys.argv[1])
ofile = open("output.out","w")

def get_no_recycled_numbers(a,b):
    no_recycled_numbers = 0
    for n in range(a,b):
        for m in range(n+1,b+1):
            strn = str(n)
            strm = str(m)

            nd = deque(strn)
            md = deque(strm)

            for i in range(0,len(md)):
                tmp = md.popleft()
                md.append(tmp)
                all_ok = True
                for i in range(0,len(md)):
                    if md[i] != nd[i]:
                        all_ok = False
                        break
                if all_ok:
                    #print strm + " " + str(md) + " " +  str(nd)
                    no_recycled_numbers+=1
                    break

    return no_recycled_numbers
                    

i = 0
for line in ifile.readlines()[1:]:
    i += 1
    words = line.strip().split()
    output_line = "Case #" + str(i) + ": " + str(get_no_recycled_numbers(int(words[0]), int(words[1])))
    ofile.write(output_line + "\n")
    print output_line 

