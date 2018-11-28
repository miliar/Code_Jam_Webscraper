#!/usr/bin/python
import sys
from string import maketrans                                                                                                                 


input = open (sys.argv[1],'r')
G = "abcdefghijklmnopqrstuvwxyz" 
E = "yhesocvxduiglbkrztnwjpfmaq"
X = int(input.readline())
for i in range(0,X):
  L = input.readline().rstrip().translate(maketrans(G,E))
  print "Case #%d: %s"% (i+1,L)
