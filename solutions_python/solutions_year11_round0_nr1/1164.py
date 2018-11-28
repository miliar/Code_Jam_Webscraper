#!/bin/python
import os, sys

filename = "A-large"

infile = open("%s.in" % filename,"rb")
outfile = open("%s.out" % filename, "wb")
T = int(infile.readline())
for index in xrange(T):
  # Get the button sequence
  items = infile.readline().split()[1:]
  items = zip(items[::2], map(int, items[1::2]))
  print items
  
  # Start the robots
  orangeSpot = 1
  blueSpot = 1
  orangeTarget = None
  blueTarget = None
  orangeDelta = None
  blueDelta = None
  
  # Find the robot targets
  for i in xrange(len(items)):
    bot, button = items[i]
    if bot == 'O' and orangeTarget is None:
      orangeTarget = i
      print "Orange target is %d" % i
      orangeDelta = button - orangeSpot + 1
      if blueTarget:
        break
    elif bot == 'B' and blueTarget is None:
      blueTarget = i
      print "Blue target is %d" % i
      blueDelta = button - blueSpot + 1
      if orangeTarget:
        break
  
  # Now, step through a simulation.
  t = 0
  while not (orangeTarget is None and blueTarget is None):
    # Figure out which bot moves
    moveBlue = True
    if orangeTarget is not None:
      if blueTarget is not None:
        moveBlue = orangeTarget > blueTarget
      else:
        moveBlue = False
    
    # Move the robot that's first in the sequence to its target.
    if moveBlue:
      advance = abs(items[blueTarget][1] - blueSpot) + 1
      blueSpot = items[blueTarget][1]
      print "Blue bot moved to %d" % blueSpot
      # Find next place to go
      for i in xrange(blueTarget + 1, len(items)):
        bot, button = items[i]
        if bot == 'B':
          blueTarget = i
          blueDelta = button - blueSpot + 1
          break
      else:
        blueTarget = None
      
      # Advance the other robot
      if orangeTarget is not None:
        if abs(items[orangeTarget][1] - orangeSpot) <= advance:
          orangeSpot = items[orangeTarget][1]
        elif items[orangeTarget][1] < orangeSpot:
          orangeSpot -= advance
        else:
          orangeSpot += advance
    else:
      advance = abs(items[orangeTarget][1] - orangeSpot) + 1
      orangeSpot = items[orangeTarget][1]
      print "Orange bot moved to %d" % orangeSpot
      # Find next place to go
      for i in xrange(orangeTarget + 1, len(items)):
        bot, button = items[i]
        if bot == 'O':
          orangeTarget = i
          orangeDelta = button - orangeSpot + 1
          break
      else:
        orangeTarget = None
      
      # Advance the other robot
      if blueTarget is not None:
        if abs(items[blueTarget][1] - blueSpot) <= advance:
          blueSpot = items[blueTarget][1]
        elif items[blueTarget][1] < blueSpot:
          blueSpot -= advance
        else:
          blueSpot += advance
    
    t += advance
    print "Advanced %d to time %d" % (advance, t)

  outfile.write("Case #%d: %d\n" % (index+1, t))