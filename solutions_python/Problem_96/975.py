import os, sys

cases = sys.stdin.readline()
loop = int(cases) + 1

for case in range(0, loop):

      data = sys.stdin.readline()
      data = data.rstrip()
      data = data.split(" ")

      if (data and "".join(data).rstrip()):  

            googlers = int(data[0])
            surprise_th = int(data[1])
            max_score = int(data[2])
            
      
            winners = 0
            surprises = 0
            loop = 3 + googlers

            for user in range(3, loop):
                  num = int(data[user])
                  if (max_score == 1 and num ==0):
                        continue
                  if ( num > (3*(max_score - 1)) ):
                        winners = winners + 1
                  elif (surprises < surprise_th): 
                        if (( num == 3*(max_score - 1)) or (num == (3*(max_score - 1) - 1) ) ):
                              surprises = surprises + 1
            total = winners + surprises           
            print "Case #"+str(case+1)+":", total
      
