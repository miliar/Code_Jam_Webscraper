#!/usr/bin/env python

import sys

_rest_tokens = []

def readToken():
  global _rest_tokens
  if not _rest_tokens:
    _rest_tokens = sys.stdin.readline().strip().split()
    _rest_tokens.reverse()
  return _rest_tokens.pop()

def log(*obj):
  is_first = True
  for o in obj:
    if not is_first:
      is_first = False
    else:
      sys.stderr.write(' ')
    sys.stderr.write(str(o))
  sys.stderr.write('\n')

def main():
  case_count = int(readToken())
  for i in range(case_count):
    log('Process case #%d' % (i + 1))
    b_time = o_time = 0
    b_pos = o_pos = 1
    total_time = 0
    move_count = int(readToken())
    while move_count > 0:
      robot_id = readToken()
      button_pos = int(readToken())
      #log('Robot ID: %s; Button pos: %d' % (robot_id, button_pos))
      if robot_id == 'B':
        action_time = abs(b_pos - button_pos) + 1
        if b_time + action_time <= o_time:
          b_time = o_time + 1
        else:
          b_time = b_time + action_time
        b_pos = button_pos
        total_time = b_time
      else:
        action_time = abs(o_pos - button_pos) + 1
        if o_time + action_time <= b_time:
          o_time = b_time + 1
        else:
          o_time = o_time + action_time
        o_pos = button_pos
        total_time = o_time
      #log('Action time: %d' % action_time)
      #log('Total time: %d' % total_time)
      move_count -= 1
    print 'Case #%d: %d' % (i + 1, total_time)
      
if __name__ == '__main__':
  main()
  
  