#!/usr/bin/env python

table = {
    'a': 'y',
    'b': 'h',
    'c': 'e',
    'd': 's',
    'e': 'o',
    'f': 'c',
    'g': 'v',
    'h': 'x',
    'i': 'd',
    'j': 'u',
    'k': 'i',
    'l': 'g',
    'm': 'l',
    'n': 'b',
    'o': 'k',
    'p': 'r',
    'q': 'z',
    'r': 't',
    's': 'n',
    't': 'w',
    'u': 'j',
    'v': 'p',
    'w': 'f',
    'x': 'm',
    'y': 'a',
    'z': 'q'
}

def translate(line):
  result = []
  words = line.split(' ')
  for word in words:
    result.append(''.join(map((lambda x: table[x]), word)))
  return ' '.join(result)

def main():
  f = open('A-small-attempt0.in')
  lines_no = int(f.readline())
  for i in xrange(lines_no):
    line = f.readline()[:-1]
    print 'Case #%d: %s' % (i + 1, translate(line))

if __name__ == '__main__':
  main()
