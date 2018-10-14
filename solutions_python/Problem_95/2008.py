

gmap = {}
gmap['a'] = 'y'
gmap['b'] = 'n'
gmap['c'] = 'f'
gmap['d'] = 'i'
gmap['e'] = 'c'
gmap['f'] = 'w'
gmap['g'] = 'l'
gmap['h'] = 'b'
gmap['i'] = 'k'
gmap['j'] = 'u'
gmap['k'] = 'o'
gmap['l'] = 'm'
gmap['m'] = 'x'
gmap['n'] = 's'
gmap['o'] = 'e'
gmap['p'] = 'v'
gmap['q'] = 'z'
gmap['r'] = 'p'
gmap['s'] = 'd'
gmap['t'] = 'r'
gmap['u'] = 'j'
gmap['v'] = 'g'
gmap['w'] = 't'
gmap['x'] = 'h'
gmap['y'] = 'a'
gmap['z'] = 'q'
gmap[' '] = ' '

if __name__ == "__main__":
  import sys
  f = sys.stdin
  T = int(f.readline().strip())
  grev = {}
  for k in gmap.keys():
    grev[gmap[k]] = k
  for i in range(T):
    sn = f.readline().strip()
    so = []
    for j in range(len(sn)):
      so.append(grev[sn[j]])
    print "Case #%d: %s" %(i+1, "".join(so))
