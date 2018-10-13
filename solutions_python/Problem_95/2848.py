import sys
from string import maketrans

mapping = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z' : 'q'}

inp = ''.join(mapping.keys())
outp = ''.join(mapping.values())
transtab = maketrans(inp, outp)


def doCase(ln):
  return ln.translate(transtab)
  

import sys

stdin = sys.stdin

num = sys.stdin.readline()

#print num

for i in xrange(int(num)):
  ln = stdin.readline()
  
  val = doCase(ln)
  sys.stdout.write( 'Case #%s: %s' % (i+1, val ) )