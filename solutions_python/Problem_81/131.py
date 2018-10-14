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
  str_obj = [str(o) for o in obj]
  sys.stderr.write(' '.join(str_obj) + '\n')
 
def main():
  case_count = int(readToken())
  for i in range(case_count):
    log('Process case #%d' % (i + 1))
    team_count = int(readToken())
    schedule = []
    for j in range(team_count):
      schedule.append(readToken())
    
    # Calc WP's
    wps_src = []
    wps = []
    for s in schedule:
      total = 0
      wins = 0
      for c in s:
        if c == '.': continue
        total += 1
        if c == '1': wins += 1
      wps_src.append((wins, total))
      wps.append(float(wins) / total)
      
    # Calc OWP's
    owps = []
    for s in schedule:
      total = 0
      count = 0
      for j in range(len(s)):
        c = s[j]
        if c == '.': continue
        count += 1
        total += float(wps_src[j][0] - (1 if c == '0' else 0)) / (wps_src[j][1] - 1)
      owps.append(total / count)

    # Calc OOWP's
    oowps = []
    for s in schedule:
      total = 0
      count = 0
      for j in range(len(s)):
        c = s[j]
        if c == '.': continue
        count += 1
        total += owps[j]
      oowps.append(total / count)
      
    result = []  
    for j in range(team_count):
      result.append(str(0.25 * wps[j] + 0.50 * owps[j] + 0.25 * oowps[j]))
    
    print 'Case #%d:\n%s' % (i + 1, '\n'.join(result))
      
if __name__ == '__main__':
  main()
