import sys
import re

dict = {}
dict['a'] = 'y'
dict['b'] = 'h'
dict['c'] = 'e'
dict['d'] = 's'
dict['e'] = 'o'
dict['f'] = 'c'
dict['g'] = 'v'
dict['h'] = 'x'
dict['i'] = 'd'
dict['j'] = 'u'
dict['k'] = 'i'
dict['l'] = 'g'
dict['m'] = 'l'
dict['n'] = 'b'
dict['o'] = 'k'
dict['p'] = 'r'
dict['q'] = 'z'
dict['r'] = 't'
dict['s'] = 'n'
dict['t'] = 'w'
dict['u'] = 'j'
dict['v'] = 'p'
dict['w'] = 'f'
dict['x'] = 'm'
dict['y'] = 'a'
dict['z'] = 'q'
dict[' '] = ' '
dict['\n'] = '\n'

def main(args):
  n = int(sys.stdin.readline())
  s = set()
  for _ in range(n):
    sys.stdout.write('Case #{0}: '.format(_ + 1))
    line = sys.stdin.readline()
    for c in line:
      sys.stdout.write(dict[c])


main(sys.argv)
