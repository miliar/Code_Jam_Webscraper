#!/usr/bin/python
import string

m = {}

def init_dict():
  m['y'] = 'a'
  m['n'] = 'b'
  m['f'] = 'c'
  m['i'] = 'd'
  m['c'] = 'e'
  m['w'] = 'f'
  m['l'] = 'g'
  m['b'] = 'h'
  m['k'] = 'i'
  m['u'] = 'j'
  m['o'] = 'k'
  m['m'] = 'l'
  m['x'] = 'm'
  m['s'] = 'n'
  m['e'] = 'o'
  m['v'] = 'p'
  m['z'] = 'q'
  m['p'] = 'r'
  m['d'] = 's'
  m['r'] = 't'
  m['j'] = 'u'
  m['g'] = 'v'
  m['t'] = 'w'
  m['h'] = 'x'
  m['a'] = 'y'
  m['q'] = 'z'

def translate(line):
  result = []
  for c in line:
    if c in string.ascii_letters:
      if c in m:
        result.append(m[c])
    else:
      result.append(c)
  return ''.join(result)

init_dict()
num_cases = input()
for i in range(1, num_cases + 1):
  cur_line = raw_input()
  output = translate(cur_line)
  print "Case #%d:" % i, output
