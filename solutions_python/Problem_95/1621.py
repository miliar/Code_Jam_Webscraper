d = dict()
d['a'] = 'y'
d['b'] = 'h'
d['c'] = 'e'
d['d'] = 's'
d['e'] = 'o'
d['f'] = 'c'
d['g'] = 'v'
d['h'] = 'x'
d['i'] = 'd'
d['j'] = 'u'
d['k'] = 'i'
d['l'] = 'g'
d['m'] = 'l'
d['n'] = 'b'
d['o'] = 'k'
d['p'] = 'r'
d['r'] = 't'
d['s'] = 'n'
d['t'] = 'w'
d['u'] = 'j'
d['v'] = 'p'
d['z'] = 'q'
d['q'] = 'z'
d['w'] = 'f'
d['y'] = 'a'
d['x'] = 'm'
    
n = int(input())
for i in range(n):
  t = input()
  print("Case #{0}: ".format(str(i+1)), end="")
  for x in t:
    if x == ' ':
      print(' ', end="")
      continue
    print(d[x], end="")
  print()
    
