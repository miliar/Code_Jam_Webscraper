#!/usr/bin/python
# -*- coding: utf-8 -*-
# @file   tidyLarge.py  
# @brief  Google Code Jam 2017 - Qualification - Problem B
# @author Laurent Sauvage <sauvage_laurent@hotmail.com>
 
# -------
# Imports
# -------
import sys          # For argv[], exit(), etc
from os import path # For abspath()

# ---------
# Functions
# ---------
def lastTidy(N_str):
#  print '='*20+"NEW num="+N_str+'='*20
   N_l= list(N_str)
   notFullScan= True 
   while notFullScan:
      notFullScan= False
      for i in range(1,len(N_l)):
         numi= int(N_l[i])
         nump= int(N_l[i-1])
         if numi<nump:
            notFullScan= True
            N_l[i-1]= str(nump-1)
            for j in range(i,len(N_l)): N_l[j]= '9'
            break
#        print "\tUPDATE N_l=", N_l
   return int("".join(N_l))

# ----
# Main
# ----
if __name__ == "__main__":

   # Initialization
   try:
      IFILE= path.abspath(sys.argv[1])

   except IndexError:
      print "Usage: %s <IFILE>" % path.basename(sys.argv[0])
      sys.exit(2) # Command line syntax error

   fdIn = open(IFILE, 'r')
   OFILE= IFILE.replace(".in",".out")
   fdOut= open(OFILE, 'w')

   # Processing
   _= int(fdIn.readline()) # Number of tests (useless with Python...)
   for nTest, l in enumerate(fdIn):
      nTest+= 1
      N_str= l.rstrip()
      line= "Case #{0}: {1}\n".format(nTest, lastTidy(N_str))
      print line,
      fdOut.write(line)

   # Termination
   fdIn .close()
   fdOut.close()
