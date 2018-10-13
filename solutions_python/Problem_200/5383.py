import math
from decimal import Decimal
#Kemisettia CodeJam Tidy Numbers
#print must have parents!!!
fire = open("B-small-attempt0.in",'r')
water = open("output.txt",'w')
iterations = fire.readline()
def isTidy(x):
 prev = 0 
 for c in str(x):
  if int(c) >= prev:
   prev = int(c)
  else:
   return False
   break
 return True

for i in range(1,int(iterations)+1):
 temp = fire.readline()
 temp = Decimal(temp)
 new = int(temp)
 if temp < 111100: 
  for hey in range(new,0,-1):
   if isTidy(hey) == True:
    water.write("Case #" + str(i) + ": " + str(hey) + "\n")
    break
 else:
  bag = 2
  while int(temp/bag) > 111100:
   bag = bag * 2
  print (bag)
  current = int(temp)
  for dev in range(0,bag):
   stobar = current
   for cre in range(stobar,stobar-(int(temp/bag))-1,-1):
    if isTidy(cre) == True:
     water.write("Case #" + str(i) + ": " + str(cre) + "\n")
     break
    else:
     current-=1