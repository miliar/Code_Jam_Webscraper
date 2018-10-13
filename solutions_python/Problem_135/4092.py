#!/usr/bin/env python

"""
python 2.6.6 

Google Code Jam 2013

Instructions:
	
	./google.py inputstatements.txt filename.in


Developed by Eunmin Lee, google code jam nickname=mgood2
All copyrights reserved by evlcode.com
"""

import warnings
from sys import argv, exit
import os
from _100000 import _100000
from _200000 import _200000

if len(argv) < 3 or '-h' in argv:
    print "usage: problem.py INPUTSTATEMENT FILENAME\n"
    exit(0)
inputstatement = argv[1]
filename = argv[2]

[T, n_A, M_AD, n_B, M_BD]=_100000(filename)
output=_200000(T, n_A, M_AD, n_B, M_BD)

for cases in range(1,int(T[0])+1):
    print("Case #%s: %s" %(cases, output[cases-1]))
