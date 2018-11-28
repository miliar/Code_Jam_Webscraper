#!/usr/bin/env python2.6
# Alien Language (90101.0)
# A submission by Cortland Klein <me@pixelcort.com>
# 2009-09-02

# import pdb; pdb.set_trace();

import pdb;

with open('A-large.in') as f:
  l, d, n = f.next().split(' ')
  l, d, n = int(l), int(d), int(n)
  
  d_array = [] # D are all the words
  for i in range(d):
    d_array.append(f.next().rstrip())
  
  n_array = [] # Are the scrambled words
  for i in range(n):
    n_array.append(f.next().rstrip())
  
  for i in range(n):
    case = i+1
    count = 0
    test = n_array[i]
    
    # Here be Dragons
    
    tokens = []
    in_a_token = False
    current_token = []
    
    # Convert test into token array
    for j in range(len(test)):
      if in_a_token:
        if test[j] == ')':
          in_a_token = False
          tokens.append(current_token)
          current_token = []
        else:
          current_token.append(test[j])
      else:
        if test[j] == '(':
          in_a_token = True
        else:
          tokens.append(test[j])
    
    # Test against all known words
    for j in d_array:
      # Assume true, try to falsify
      is_a_match = True
      
      for k in range(l): # l is always the magical length of known words
        if is_a_match:
          if not j[k] in tokens[k]:
            is_a_match = False
      if is_a_match:
        count = count+1
      
    
    # There be Dragons
    
    print "Case #" + str(case) + ": " + str(count)
  
  #import pdb; pdb.set_trace();