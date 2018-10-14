#!/usr/bin/env python
# encoding: utf-8
"""
FlySwat.py

Created by Graham Dennis on 2008-06-18.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import getopt
import math

help_message = '''
The help message goes here.
'''


class Usage(Exception):
  def __init__(self, msg):
    self.msg = msg


def main(argv=None):
  if argv is None:
    argv = sys.argv
  try:
    try:
      opts, args = getopt.getopt(argv[1:], "ho:v", ["help", "output="])
    except getopt.error, msg:
      raise Usage(msg)
  
    # option processing
    for option, value in opts:
      if option == "-v":
        verbose = True
      if option in ("-h", "--help"):
        raise Usage(help_message)
      if option in ("-o", "--output"):
        output = value
  
  except Usage, err:
    print >> sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
    print >> sys.stderr, "\t for help use --help"
    return 2
  
  fd = file(args[0])
  
  numCases = int(fd.next())
  
  caseNum = 1
  
  for line in fd:
    f, R, t, r, g = map(float, line.split())
    # Inside each g*g square, there is a smaller square in which the fly
    # would live if its centre was within it.
    innerRadius = R-t-f
    innerRadius2 = innerRadius**2
    flyLivesSquareLength = g - 2*f
    if flyLivesSquareLength < 0.0:
      probabilityOfDeath = 1.0
    else:
      flyLivesSquareArea = flyLivesSquareLength**2
      areaOfLife = 0.0
      # Consider each 'life square' in turn
      # But only for one quadrant, as each quadrant is the same, so choose top-right.
      xStart = yStart = r + f
      x = y = xStart
      while y < R-t:
        while x*x + y*y < innerRadius2:
          xEnd = x + flyLivesSquareLength
          yEnd = y + flyLivesSquareLength
          if xEnd*xEnd + yEnd*yEnd > innerRadius2:
            # The 'life square' is partially obscured by the edge
            # of the racquet.
            
            xTopLeft = x
            yTopLeft = y + flyLivesSquareLength
            if (xTopLeft**2 + yTopLeft**2) < innerRadius2:
              # Calculate the area before the circle intersects
              areaOfLife += flyLivesSquareLength*(math.sqrt(innerRadius2-yTopLeft**2)-x)
              xArcStart = math.sqrt(innerRadius2-yTopLeft**2)
            else:
              xArcStart = xTopLeft
            # Two cases, circle intersects bottom side, or circle intersects right side.
            xBottomRight = x + flyLivesSquareLength
            yBottomRight = y
            if (xBottomRight**2 + yBottomRight**2) < innerRadius2:
              xArcStop = xBottomRight
            else:
              xArcStop = math.sqrt(innerRadius2 - yBottomRight**2)
            
            # Integral of sqrt(R^2-x^2)
            F = lambda xp: 0.5*(xp*math.sqrt(innerRadius2-xp**2) + innerRadius2*math.asin(xp/innerRadius))
            areaUnderCurve = F(xArcStop) - F(xArcStart) - (xArcStop-xArcStart)*y
            areaOfLife += areaUnderCurve
            
          else:
            areaOfLife += flyLivesSquareArea
          x += g + 2*r
        x = xStart
        y += g + 2*r
      
      areaOfLife *= 4.0 # Four quadrants
      totalArea = math.pi*R*R
      probabilityOfLife = areaOfLife/totalArea
      probabilityOfDeath = 1.0 - probabilityOfLife
    print "Case #%(caseNum)s: %(probabilityOfDeath)f" % locals()
    caseNum += 1


if __name__ == '__main__':
    main()

