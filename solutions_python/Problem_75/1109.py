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
    opposes = {}
    transforms = {}
    result = ''
    for j in range(int(readToken())): # Read transforms
      token = readToken()
      t_key = token[:2]
      t_result = token[2:]
      transforms[t_key] = t_result
      transforms[t_key[::-1]] = t_result
    for j in range(int(readToken())): # Read opposes
      token = readToken()
      key1 = token[0]
      key2 = token[1]
      opposes[key1] = key2
      opposes[key2] = key1
    letter_count = int(readToken())
    for c in readToken():
      result += c
      while len(result) >= 2 and result[-2:] in transforms:
        result = result[:-2] + transforms[result[-2:]]
      if result[-1:] in opposes and result.find(opposes[result[-1:]]) >= 0:
        result = ''
    ans = '['
    for c in result:
      ans += c + ', '
    if len(ans) > 1:
      ans = ans[:-2]
    ans += ']'
    print 'Case #%d: %s' % (i + 1, ans)
      
if __name__ == '__main__':
  main()
