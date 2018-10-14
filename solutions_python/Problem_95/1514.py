#!/usr/bin/env python
import sys

KEY_IN = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
          'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
          'de kr kd eoya kw aej tysr re ujdr lkgc jv']

KEY_OUT = ['our language is impossible to understand',
           'there are twenty six factorial possibilities',
           'so it is okay if you want to just give up']

KEY = {'z':'q', 'q':'z'}

for i in range(len(KEY_IN)):
  ki = KEY_IN[i]
  ko = KEY_OUT[i]
  for j in range(len(ki)):
    KEY[ki[j]] = ko[j]

if __name__ == '__main__':
  N = int(sys.stdin.readline())
  for i in range(N):
    input = sys.stdin.readline().strip()
    output = ''.join(KEY[c] for c in input)
    print('Case #%d: %s' % (i+1, output))

