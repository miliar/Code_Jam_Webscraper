a = {' ': ' ',
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
    'z': 'q'}
import sys

k = 0
n = int(sys.stdin.readline().rstrip())
for j in range(n):
  line = sys.stdin.readline().rstrip()
  k += 1
  out = ""
  for i in range(len(line)):
    out += a[line[i]]
  print "Case #%s: %s" % (str(k), out)
