#!/usr/bin/env python

def check_one_digit(s, i):
  for j in range(i+1,len(s)):
    if s[i] < s[j]:
      s = ''.join(['9' for _ in range(0,j)]) + chr(ord(s[j])-1) + s[j+1:]
      break
  return s

with open('B-large.in') as f:
  T = int(f.readline())
  with open('B-large.out', 'w') as of:
    for t in range(0,T):
      s = f.readline().strip()
      s = s[::-1]
      for i in range(0,len(s)):
        s = check_one_digit(s, i)
      s = s[::-1]
      if s[0] == '0':
        s = s[1:]
      of.write('Case #' + str(t+1) + ': ' + s + '\n')
