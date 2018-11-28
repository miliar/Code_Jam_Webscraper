import copy
import fractions
import os
import re
import string
import sys
import time

min_minutes = 0xFFFFFFFF
def recursive(plates, minutes):
   global min_minutes
   
   # Next minute
   minutes += 1
   
   # Quit if we are passed the straightforward answer
   if (minutes > min_minutes):
      return

   # If we finished all the plates
   if (plates[len(plates)-1] == 1):
      if (minutes < min_minutes):
         min_minutes = minutes
      return   
   
   # Still more work
   else:
      
      # Try eating this round
      plates1 = copy.copy(plates)
      plates1 = map(lambda x: x-1, plates1)
      recursive(plates1, minutes)
   
      # Try distributing the max
      max_value = plates[len(plates)-1]
      if (max_value > 1):
         
         # Find the large factor or split in half
         new_value = 0
         for i in range(2, max_value/2+1):
            
            if (fractions.gcd(max_value, i) == i):
               new_value = i
         
         if (new_value == 0): new_value = max_value/2
         plates[len(plates)-1] = new_value
         plates.append(max_value - new_value)
         plates = sorted(plates)
         recursive(plates, minutes)
   
start = time.time()

filename = sys.argv[1]
file = open(filename, "rb")

cases = int(file.readline())
for case in range(1, cases+1):
   
   sys.stderr.write("%d\n" % (case))
   
   dummy = int(file.readline())
   plates = sorted(map(int, string.split(file.readline())))
   min_minutes = plates[len(plates)-1]
   recursive(plates, 0)
   
   print "Case #%d: %d" % (case, min_minutes)
   
file.close()

end = time.time()

sys.stderr.write("%f\n" % (end-start))
