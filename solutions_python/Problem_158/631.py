import copy
import fractions
import os
import re
import string
import sys
import time

start = time.time()

filename = sys.argv[1]
file = open(filename, "rb")

cases = int(file.readline())
for case in range(1, cases+1):
   
   # sys.stderr.write("%d\n" % (case))
   
   temp = file.readline().split()
   x = int(temp[0])
   r = int(temp[1])
   c = int(temp[2])
   
   # GABRIEL
   if ((x <= 6) and 
       (max(r, c) >= x) and 
       (min(r, c) > min(x-2, x/2+x%2)) and 
       ((r*c%x) == 0)):
      
      winner = "GABRIEL"
   
   else:
   
      winner = "RICHARD"
      
   print "Case #%d: %s" % (case, winner)
   
file.close()

end = time.time()

sys.stderr.write("%f\n" % (end-start))
