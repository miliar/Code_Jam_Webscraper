import re

stuff = open("C-small-attempt0.in").readlines()
case = 1
n=stuff[0]
rec = 1

while rec < len(stuff)-1:
   line1 = re.split(" ",stuff[rec])
   line2 = re.split(" ",stuff[rec+1])
   line1 = map(int,line1)
   line2 = map(int,line2)
   summ = 0
   maxx = line1[1]
   
   # Do for all time roller coaster rides
   for i in range(line1[0]):
       smallsum = 0
       rollergroup = []
       while True:
           try:
               if smallsum + line2[0] <= maxx:
                   x = line2.pop(0)
                   smallsum = smallsum + x
                   rollergroup.append(x)
               else:
                    line2.extend(rollergroup)
                    summ = smallsum + summ
                    break
           except:
               line2.extend(rollergroup)
               summ = smallsum + summ
               break
   print "Case #%d: %d" % (case,summ)
   
   case = case + 1
   rec = rec + 2
