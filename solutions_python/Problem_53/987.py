#!env python

import sys
import array

NOPOWER_OFF = 0
NOPOWER_ON = 1
POWER_OFF = 2
POWER_ON = 3

def main():
  num_cases = int(sys.stdin.readline().strip())
  for i in range(1,num_cases+1):
    (ns,ks) = sys.stdin.readline().split()
    (n,k) = (int(ns), int(ks))
    ss = array.array('H')
  
    # initialize
    ss.append(POWER_ON) # wall socket
    ss.append(POWER_OFF) 
    for j in range(2, n+1):
      ss.append(NOPOWER_OFF)

    for j in range(k):  #snaps
      # first, react to snap
      for m in range(1,n+1): # update state
        ss[m] = snap(ss[m])

      # next, react to power 
      for m in range(1,n+1): # update state
        if (isLit(ss[m-1])):
          ss[m] = power(ss[m])
        else:
          ss[m] = unpower(ss[m])

    print ("Case #" + str(i) + ": " + format(ss[n]));


def power(x):
  if x == NOPOWER_OFF or x  == NOPOWER_ON:
    return (x+2)
  else: 
    return x

def unpower(x):
  if x == POWER_OFF or x  == POWER_ON:
    return (x-2)
  else: 
    return x

def snap(x):
  if x == POWER_OFF:
    return POWER_ON
  elif x == POWER_ON:
    return POWER_OFF
  else:
    return x

def isLit(x):
  return isPowered(x) and isOn(x)

def isOn(x):
  return (x == 1 or x == 3)

def isPowered(x):
  return (x == 2 or x == 3)

def format(x):
  if isLit(x):
    return "ON" 
  else:
    return "OFF"

main()
