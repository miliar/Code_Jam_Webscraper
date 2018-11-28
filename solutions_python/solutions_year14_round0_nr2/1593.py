#!/usr/bin/env python

import sys

def read():
  content = ''
  for line in sys.stdin:
    content += line
  return content

def main():
  content = read()
  lines = content.split('\n')
  cases = int(lines[0])
  lines = lines[1:]
  for i in range(cases):
    line = lines[i]
    nums = [ float(x) for x in line.split(' ') ]
    C = nums[0]
    F = nums[1]
    X = nums[2]
    R = X-C
    t = 0
    j = 2
    tr = 0
    k = 0
    while j < (X-C)*F/C:
      k += 1
      t += C/j
      j += F
    tr = t
    t += X/j
    ans = 0
    if(k==0):
      ans = t
    else:
      j -= F
      tr += X/j - C/j
      ans = min(t,tr)
      if ans < 0:
        ans = max(t,tr)
    print 'Case #%d: %f'%((i+1),ans)



if __name__ == '__main__':
  main()
