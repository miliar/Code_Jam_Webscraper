#!/usr/bin/env python

import fileinput
import math

def line_line_intersection(x1, y1, x2):
  return x2 * y1 / x1

def calculate_segment_area(R, x1, y1, x2, y2, Xlow, Ylow):
  # return area of segment between x and y minus below
  # Xlow and Ylow
  #print R, x1, y1, x2, y2, Xlow, Ylow
  C = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
  segment_area = R ** 2 * math.asin(C / 2.0 / R)
  # find points of intersection of radii with Xlow and Ylow
  a1 = line_line_intersection(x1, y1, Xlow)
  a2 = line_line_intersection(x2, y2, Xlow)
  b2 = line_line_intersection(y1, x1, Ylow)
  area_a = 0.5 * Xlow * (a2 - a1)
  area_b = 0.5 * (Ylow - a1) * (b2 - Xlow)
  # area_c only if x2 > Xlow
  if x2 > Xlow:
    area_c = 0.5 * (x2 - Xlow) * (y2 - a2)
  else:
    area_c = 0.0
  if y1 > Ylow:
    area_d = 0.5 * (y1 - Ylow) * (x1 - b2)
  else:
    area_d = 0.0
  return segment_area - area_a - area_b + area_c + area_d

def line_circle_intersection(X, R):
  y2 = R * R - X * X
  if y2 < 0:
    return None
  else:
    return y2 ** 0.5

def calculate_area(X, Y, S, R):
  # (X, Y) is centre of square
  # S is side length of square
  # R is radius of circle, centred at (0, 0)
  # calculate area of intersection of square and circle
  Xlow = X - 0.5 * S
  Xhigh = X + 0.5 * S
  Ylow = Y - 0.5 * S
  Yhigh = Y + 0.5 * S
  # First find points of intersection with left and bottom
  # of square:
  int_left = line_circle_intersection(Xlow, R)
  if int_left is None or int_left <= Ylow:
    return 0
  int_bottom = line_circle_intersection(Ylow, R)
  if int_bottom is None or int_bottom <= Xlow:
    return 0
  int_right = line_circle_intersection(Xhigh, R)
  int_top = line_circle_intersection(Yhigh, R)
  if int_right is not None and int_right >= Yhigh:
    # this condition is equivalent to the corresponding one for int_top
    return S * S
  # Now the hard part
  if Ylow <= int_left <= Yhigh and Xlow <= int_bottom <= Xhigh:
    area = calculate_segment_area(R, int_bottom, Ylow, Xlow, int_left, Xlow, Ylow)
  elif Ylow <= int_left <= Yhigh:
    area = calculate_segment_area(R, Xhigh, int_right, Xlow, int_left, Xlow, Ylow)
  elif Xlow <= int_bottom <= Xhigh:
    area = calculate_segment_area(R, int_bottom, Ylow, int_top, Yhigh, Xlow, Ylow)
  else:
    area = calculate_segment_area(R, Xhigh, int_right, int_top, Yhigh, Xlow, Ylow)
  if area < 0 or area > S ** 2:
    print X, Y, S, R, '->', area
  return area

def calculate(f, R, t, r, g):
  # calculate total area of squares of gap, with size (g-2*f)
  # and divide by (Pi*R^2), and return.
  # squares occur every (g+2*r) in both dimensions, starting
  # centred at (r+g/2).
  # areas of squares actually have to be calculated as areas
  # of squares intersected with a circle of radius (R-t-f)
  # centred at the origin.
  # actually calculate gap area for the 1st quadrant, and
  # multiply by 4.
  total = 0.0
  i = 0
  while True:
    centreX = (i + 0.5) * (g + 2 * r)
    j = 0
    while True:
      centreY = (j + 0.5) * (g + 2 * r)
      area = calculate_area(centreX, centreY, g - 2.0 * f, R - t - f)
      if area == 0.0:
        break
      total += area
      j += 1
    if not j:
      break
    i += 1
  return 1.0 - total * 4 / (math.pi * R * R)

f = fileinput.input()
for i in range(1, 1 + int(f.readline())):
  print "Case #%d: %0.6f" % (i, calculate(*map(float, f.readline().split())))
