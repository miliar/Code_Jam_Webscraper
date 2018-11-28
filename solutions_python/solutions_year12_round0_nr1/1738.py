#!/usr/bin/python

fin = open('A-small-attempt0.in', 'r')
fout = open('A-small.out', 'w')

cyph = dict()
cyph['a'] = 'y'
cyph['b'] = 'h'
cyph['c'] = 'e'
cyph['d'] = 's'
cyph['e'] = 'o'
cyph['f'] = 'c'
cyph['g'] = 'v'
cyph['h'] = 'x'
cyph['i'] = 'd'
cyph['j'] = 'u'
cyph['k'] = 'i'
cyph['l'] = 'g'
cyph['m'] = 'l'
cyph['n'] = 'b'
cyph['o'] = 'k'
cyph['p'] = 'r'
cyph['q'] = 'z'
cyph['r'] = 't'
cyph['s'] = 'n'
cyph['t'] = 'w'
cyph['u'] = 'j'
cyph['v'] = 'p'
cyph['w'] = 'f'
cyph['x'] = 'm'
cyph['y'] = 'a'
cyph['z'] = 'q'

T = int (fin.readline ())

for i in range ( 1, T + 1 ):
  lin = fin.readline ()
  for j in range(len(lin)):
    if lin[j] != ' ' and lin[j] != '\n':
      #print lin[j], cyph[lin[j]]
      lin = lin[0:j] + cyph[lin[j]] + lin[j+1:]
  fout.write ("Case #%d: %s" % ( i, lin ) )

