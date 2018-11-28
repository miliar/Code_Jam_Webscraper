# Developed in Python 3.5.2
# Ran on repl.it
import functools

# Parse input
T = int(input())

for i in range(1, T+1):
  # Variables
  j = 0
  flipCounter = 0
  flipPos = set()
  flipFind = False
  
  # Parse test cases
  tokens = str(input()).split()
  pancakes = tokens[0]
  K = int(tokens[1])
  length = len(pancakes)
  
  # Flip each pancake sequentially, from 0 to length-K
  # Go through the rest of the string without flipping afterward
  for p in pancakes:
    # Update flipFind
    if j in flipPos:
      flipFind = not(flipFind)
      
    # Flip (or not) if needed
    if (not(flipFind) and p == '-') or (flipFind and p == '+'):
      if length - K < j:
        flipCounter = -1
      else:
        flipCounter += 1
        flipPos.add(j + K)
        flipFind = not(flipFind)
    
    j += 1
  
  if flipCounter < 0:    
    print("Case " + str(i) + ": IMPOSSIBLE")
  else: 
    print("Case " + str(i) + ": " + str(flipCounter))