def win(l):
  if l.count('.')==0:
    if l.count('O')==0:
      return 'X'
    elif l.count('X')==0:
      return 'O'
  return None

fi = open('input.txt', 'r')
fo = open('output.txt', 'w')
n  = int(fi.readline())
for nn in range(n):
  r = None
  bord = []
  for i in range(4):
    bord.append(fi.readline().strip())
  fi.readline()
  
  #horizontal
  for l in bord:
    r = win(l)
    if r:
      fo.write('Case #%d: %s won\n'%(nn+1, r))
      break
  if r:
    continue
  
  #vertical
  for i in range(4):
    l=''
    for ii in range(4):
      l += bord[ii][i]
    r = win(l)
    if r:
      fo.write('Case #%d: %s won\n'%(nn+1, r))
      break
  if r:
    continue
  
  #slash
  l=''
  for i in range(4):
    l+=bord[i][i]
  r = win(l)
  if r:
    fo.write('Case #%d: %s won\n'%(nn+1, r))
    continue
  
  #slash2
  l=''
  for i in range(4):
    l+=bord[i][3-i]
  r = win(l)
  if r:
    fo.write('Case #%d: %s won\n'%(nn+1, r))
    continue
    
  #draw or not end
  l=''
  for i in range(4):
    l += bord[i]
  if l.count('.'):
    fo.write('Case #%d: %s'%(nn+1, 'Game has not completed\n'))
  else:
    fo.write('Case #%d: %s'%(nn+1, 'Draw\n'))
    