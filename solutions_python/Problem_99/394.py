#!/usr/bin/env python
# encoding: utf-8
"""
password.py

Created by Alice Lieutier on 2012-04-28.
Copyright (c) 2012
"""

import sys


def process(input, output):
  nb = int(input.readline().rstrip())
  
  for val in range(1, nb+1):
    
    print("Case ",val)
    
    # reading data
    inputs = input.readline().rstrip().split()
    
    typed = int(inputs[0])
    total = int(inputs[1])
     
    proba = list(map(float,input.readline().rstrip().split()))

    print(proba)

    typing = (meanProba(proba) * (total - typed + 1) + (1 - meanProba(proba)) * (total - typed + 2 + total))
    
    b = backspace(total, proba, typed)

    answer = min(typing, b , total + 2)
    print("anwser :",answer)
    output.write('Case #%d: %s\n' % (val,answer))
    

def scalar(vector1, vector2):
  """scalar product of vectors 1 and 2
  vector1 and vector2 must be of same length
  throws exception
  """
  assert (len(vector1) == len(vector2))
  
  return sum([ a * b for a, b in zip(vector1, vector2)])
  
def meanProba(vector):
  result = 1
  for a in vector:
    result *= a
  
  return result
   
 
def backspace(total, proba, typed):
  result = list()
  for bs_nb in range(1,typed + 1):
    
    proba_ok = meanProba(proba[:(typed - bs_nb)] + [1 for i in range(bs_nb)])
    a = (bs_nb + total - typed + bs_nb + 1 ) * proba_ok
    b = (total - typed + 2 + bs_nb + total + 1) * (1-proba_ok)
    result.append(a+b)
    
  return min(result)
 



  
if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Need file as argument")
    sys.exit(1)

  input_file = sys.argv[1]

  # open the file
  input_handler = open(input_file, 'r')
  output_handler = open(input_file + '.out', 'w+')

  process(input_handler, output_handler)

  # close files
  input_handler.close()
  output_handler.close()
