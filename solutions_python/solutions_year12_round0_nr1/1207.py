'''
Created on 14.04.2012

@author: max
'''
from itertools import izip

def main():
  out = []
  charmap = enhance(train())

  for i, line in enumerate(get_input('A-small-attempt0.in')):
    out.append('Case #%i: ' % (i+1) + translate(line, charmap))
  open('output.txt', 'w+').write("\n".join(out))

def get_input(fname):
  f = open(fname, 'r')
  f.readline() # screw the 1st line
  return [l.strip() for l in f if l]

def train():
  input = ''.join((
    'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv',
  ))
  output = ''.join((
    'our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up',
  ))
  return dict(izip(input, output))

def enhance(charmap):
  charmap['q'] = 'z'
  charmap['z'] = 'q'
  return charmap

def translate(line, charmap):
  return ''.join([charmap[c] for c in line])

main()
