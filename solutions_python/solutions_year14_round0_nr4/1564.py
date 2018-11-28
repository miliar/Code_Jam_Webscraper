#!/usr/bin/env python

import sys

def read():
  result = ''
  for line in sys.stdin.readlines():
    result += line
  return result

def main():
  content = read()
  lines = content.split('\n')
  cases = int(lines[0])
  lines = lines[1:]
  for i in range(cases):
    case = i+1
    sublines = lines[0:3]
    lines = lines[3:]
    naomi = sorted([ float(x) for x in sublines[1].split(' ') ])
    ken   = sorted([ float(x) for x in sublines[2].split(' ') ])
    #print naomi
    #print ken
    # War
    k = 0
    j = 0
    m = 0
    while j < len(naomi) and k < len(ken):
      naomi_play = naomi[j]
      j += 1
      while k < len(ken) and ken[k] <= naomi_play:
        k += 1
      if k < len(ken):
	m += 1
        k += 1
    war_score = len(naomi) - m
    # Deceitful War
    k = len(ken)-1
    j = len(naomi)-1
    m = 0
    while k >= 0 and j >= m:
      ken_play = ken[k]
      if naomi[j] > ken_play:
        j -= 1
        k -= 1
      else:
        m += 1
        k -= 1
    deceitful_war_score = len(naomi) - m
    print 'Case #%d: %d %d'%(case, deceitful_war_score, war_score)



if __name__ == '__main__':
  main()
