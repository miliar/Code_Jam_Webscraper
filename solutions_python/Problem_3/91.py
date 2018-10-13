#!/usr/bin/env python
# Google Code Jam 2008 Qualifcations, Task C
# Solution by Sebastian Hagen
# language: Python 2.5
# This program reads input from stdin and writes output to stdout.

import math
from math import sin,cos,asin,acos,pi

def p_ring(R, t, f):
   safe_r = (R-t-f)
   if (R == 0):
      return 0
   return 1-(safe_r*safe_r*math.pi/(R*R*math.pi))

def p_string(g, r, f):
   if (g <= 2*f):
      return 1
   safe_area = (g-2*f)*(g-2*f) # safe empty inner squares
   tile_area = (g+2*r)*(g+2*r) # tile area
   return 1-(safe_area/tile_area)

def p_tot(f, R, t, r, g):
   pr = p_ring(R, t, f)
   ps = p_string(g, r, f)
   return pr+ps*(1-pr)

class FlySwat:
   def __init__(self, f, R, t, r, g):
      self.f = 1.0*f
      self.R = 1.0*R
      self.t = 1.0*t
      self.r = 1.0*r
      self.g = 1.0*g
      
      self.iR = iR = max(self.R - self.t - self.f,0) # radius for area not threatened by ring
      # equivalent relative values for unit circle
      self.ur = r/iR
      self.uf = f/iR
      self.ug = g/iR
   
   @staticmethod
   def stringcap_area_get(angle0, angle1):
      # circle segment formula taken from
      # <http://en.wikipedia.org/wiki/Circular_segment>
      assert (angle0 <= angle1)
      y0 = sin(angle0)
      y1 = sin(angle1)
      x0 = cos(angle0)
      x1 = cos(angle1)
      assert (x0 >= x1)
      segment_angle = angle1 - angle0
      # circle segment + right triangle next to circle segment
      return (0.5 * (segment_angle - sin(segment_angle))) + ((x0-x1) * (y1-y0) * 0.5)

   def p_collision_ring_get(self):
      if (self.R == 0):
         return 0
      return 1-(self.iR*self.iR*math.pi/(self.R*self.R*math.pi))

   def st_string_area_get(self):
      """Calculates the proportion of the area not threatened (covered or
         within f of being covered) by the ring, but threatened by one specific
         set of strings (horizontal or vertical; the two values are
         always equal).
         Also returns the proportion of area doubly threatened as second
         element in retval."""
      # The task description provides us with two axes of symmetry we can
      # exploit, so to simplify things, we'll only calculate the proportion
      # for the upper right quadrant.
      # In addition, all calculations are performed on a unit circle.

      area = 0
      area_overlaid = 0
      
      offset = -self.ur
      while (offset < 1):
         y_min = max(offset-self.uf,0)
         y_max = min(offset+2*self.ur+self.uf, 1)
         x_max = cos(asin(y_max))
         x_min = cos(asin(y_min))
         area += self.stringcap_area_get(asin(y_min), asin(y_max)) + (x_max*(y_max-y_min))
         
         x = 0
         x_l = 0
         x_h = self.ur+self.uf
         while (x_l < x_min):
            if (x_h > 1):
               x_h = 1
            if (x_h > x_max):
               area_overlaid += self.stringcap_area_get(max(acos(x_h),asin(y_min)), min(acos(x_l), asin(y_max)))
               if (x_h < x_min):
                  # Corner case: Area below right triangle computed by stringcap_area_get call above
                  area_overlaid += (x_h - max(x_l,x_max))*(sin(acos(x_h))-y_min)
               if (x_l < x_max):
                  # Area doubly threatened here but not impacted by circle arc
                  area_overlaid += (y_max-y_min)*(x_max-x_l)
            else:
               area_overlaid += (y_max-y_min)*(x_h-x_l)
            x += self.ug+2*self.ur
            x_l = x - (self.ur+self.uf)
            x_h = x + (self.ur+self.uf)

         offset += self.ug + 2*self.ur

      return (area/pi*4, area_overlaid/pi*4)
   
   def p_collision_get(self):
      """Return total probability for a swatter-fly collision"""
      (s_p, o) = self.st_string_area_get()
      p_ring = self.p_collision_ring_get()
      return (s_p*2-o)*(1-p_ring) + p_ring
   
   @classmethod
   def build_from_file(cls, f):
      (f, R, t, r, g) = [float(x) for x in f.readline().strip().split()]
      return cls(f, R, t, r, g)

   @classmethod
   def solve_from_file(cls, f):
      fs = cls.build_from_file(f)
      return fs.p_collision_get()


if (__name__ == '__main__'):
   import sys
   tc_count = int(sys.stdin.readline().strip())
   for i in range(tc_count):
      sys.stdout.write('Case #%d: %f\n' % (i+1, FlySwat.solve_from_file(sys.stdin)))


