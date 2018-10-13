#!/usr/bin/python -tt
import sys
import math

def findmoves(l1, l2,c1, c2):

  if len(l1) == 0:
    return 0;
  if l1[0] == 0:
    l1, l2 = l2, l1
    c1, c2 = c2, c1
  aim1 = aim2 = 0  
  
  #Find the next aimed value of l2
  for i in range(0, len(l2)):
    if l2[i] != 0:
      aim2 = l2[i]
      break
  aim1 = l1[0]
  moves = 0
  sign1 = sign2 = 0
  if math.fabs(aim1 - c1) == math.fabs(aim2 - c2):
    #Both have to move equal moves.
    moves = math.fabs(aim1 - c1) + 1
    # + 1 done for pushing button.
    c1 = aim1
    c2 = aim2
  else:
    moves = math.fabs(aim1 - c1) + 1
    t1 = c1
    c1 = aim1
    if math.fabs(aim1 - t1) < math.fabs(aim2 - c2):
      c2 = c2 + math.copysign(moves, aim2 - c2)
    else:
      c2 = aim2  
    
    
  l1.pop(0)
  l2.pop(0)
  return moves + findmoves(l1, l2, c1, c2)
      
  
def bottrust():
  filename = sys.argv[1]
  input_file = open(filename, 'r')
  # get the number of cases
  num_of_cases = int(input_file.readline())
  for i in range(1, num_of_cases + 1):
    il = [x for x in list(input_file.readline().strip().split())]
    il.pop(0)
    
    
    
    l1 = []
    l2 = []
    while (len(il)):
      type = il.pop(0)
      if (type == 'O'):
        l1.append(int(il.pop(0)))
        l2.append(0)
      else:
        l2.append(int(il.pop(0)))
        l1.append(0)
        
    
    print "Case #" + str(i) + ": " + str(int(findmoves(l1, l2, 1, 1)))
          
       
 

if __name__ == '__main__':
  bottrust()