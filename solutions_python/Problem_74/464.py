#! /usr/bin/env python

import os
import sys
import math
import copy
import numpy as np


class robot():
  def __init__(self, buttons):
    self.buttons = buttons;
    self.pos = 1;
    self.t = 0;

  def move(self, t):
    ''' moves the robot towards the next button for t sec (as far as it can) '''
    if len(self.buttons) > 0:
      # distance between robot and next button
      d = abs(self.buttons[0] - self.pos);

      # new position
      dm = min(d, t);
      self.pos = self.pos + np.sign(self.buttons[0] - self.pos)*dm;

    # increment time
    self.t += t;

  def press(self):
    ''' presses the button '''
    self.buttons.pop(0);

    # takes 1sec to press a button
    self.t += 1;
    return 1;

  def move_to_next(self):
    ''' moves the robot to the next button '''
    # distance between robot and next button
    d = abs(self.buttons[0] - self.pos);
    self.t += d;

    # set new position
    self.pos = self.buttons[0];

    # return time to get there
    return d;



def parse_line(l):
  ''' 
    returns 3 lists 
    order = [blue, orange, ...]
    blue buttons
    orange buttons
  '''
  i = 1;
  order = [];
  blue = [];
  orange = [];
  
  while i < len(l):
    r = l[i];
    order.append(r);
    if r == 'O':
      orange.append(int(l[i+1]));
    elif r == 'B':
      blue.append(int(l[i+1]));
    else:
      print 'PARSE ERROR';

    i+=2;
      
  return (order, blue, orange);

def compute_time(order, blue, orange):
  B = robot(blue);
  O = robot(orange);

  # iterate over button presses
  for r in order:
    if r == 'O':
      d = O.move_to_next();
      d += O.press();
      B.move(d);
    elif r == 'B':
      d = B.move_to_next();
      d += B.press();
      O.move(d);
    else:
      print 'COMPUTE ERROR'

  return max(B.t, O.t);

if __name__=='__main__':
  f = open(sys.argv[1], 'r');
  T = int(f.readline());

  case = 0;
  for n in np.arange(T):
    case += 1;
    l = f.readline().split();
    (order, blue, orange) = parse_line(l);
    t = compute_time(order, blue, orange);
    print 'Case #%d: %d' % (case, t);

    


