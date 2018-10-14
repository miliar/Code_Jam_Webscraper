'''
Created on Sep 3, 2009

@author: mech
'''

import re

infile = open ("in1", "r")
L,D,N = [ int(i) for i in infile.readline().split() ]

words = ""

for i in range(0,D):
    words = words + infile.readline()
    
for i in range(0,N):
    pattern = infile.readline().rstrip()
    pattern = re.sub ('\(','[', pattern)
    pattern = re.sub ('\)',']', pattern)
    print "Case #" + str(i+1) + ": " + str(len(re.findall(pattern, words)))