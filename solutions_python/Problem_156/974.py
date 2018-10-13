#!/usr/bin/env python

from sys import stdin


def find_max(v):
  max_n = 0; max_i=0
  for x in range(len(v)):
    if v[x] > max_n:
      max_n = v[x]
      max_i = x
  return max_i

cases = int(stdin.readline())

for c in range(cases):
  n_plates = int(stdin.readline())
  plates = stdin.readline()[:-1].split()
  plates = [ int(x) for x in plates ]
    
  #print plates
  nodes = [ ( 0, plates ) ]
  
  best_minutes = max(plates)
  while len(nodes) > 0:
    minutes, plates = nodes.pop()
    if minutes >= best_minutes:
      continue
    max_plates = max(plates)
      
    if max_plates < 4:
      minutes += max_plates
      if minutes < best_minutes:
        best_minutes = minutes

    else:
      max_i = find_max( plates )

      for split in range(2,int(plates[max_i] / 2)+1):
        new_plates_split = list(plates)
        new_plates_split[max_i] -= split
        new_plates_split.append(split)
      
        nodes.append( ( minutes+1, new_plates_split ) )
      
      new_plates_eat = map( lambda x: x-1 if x > 0 else 0, plates )
  
      nodes.append( ( minutes+1, new_plates_eat ) )
 
  print "Case #%d: %d" %(c+1, best_minutes)
