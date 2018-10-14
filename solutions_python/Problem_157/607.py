infile = 'C-small-attempt0.in'
outfile = 'C-small-out.txt'

import math

quat = {'ii': [-1, '1'], 
        'ij': [1, 'k'], 
        'ik' : [-1,'j'],
        'ji': [-1, 'k'], 
        'jj': [-1, '1'], 
        'jk': [1, 'i'],
        'ki': [1, 'j'], 
        'kj': [-1, 'i'], 
        'kk': [-1, '1']}

def prod(x, letter):
  if x[1] == '1':
    return [x[0], letter]
  p = quat[x[1]+letter]
  return [x[0]*p[0], p[1]]

def check(ph, times):
  phrase = ph*times
  if len(phrase) < 3: 
    return 'NO'
  target = 'ijk'
  k = 0  
  reset = True
  frag = ''
  
  for i in xrange(len(phrase)):
    if reset:
      if frag == '':
        frag = [1, phrase[i]]
      else:
        reset = False
    if not reset:
      frag = prod(frag, phrase[i]) 
    if k <= 1:
      if frag[0] == 1 and frag[1] == target[k]:
        reset = True
        k += 1
        frag = ''
    #print i, frag, reset
  if k == 2 and frag[0] == 1 and frag[1] == target[k]:
    return 'YES'
  else:
    return 'NO'


def main():
  out = open(outfile, 'w')
  f = open(infile)
  N = int(f.readline())
  for n in xrange(N):
    times = int(f.readline().split()[1])
    ph = f.readline().strip()
    #print times, ph
    out.write("Case #"+str(n+1)+": "+check(ph, times)+"\n")


main()

