fname = 'D-large'
fin = open('%s.in' % fname,'r')
fout = open('%s.out' % fname,'w')

T = int(fin.readline())

for i in range(T):
  pts_war = 0
  pts_dwar = 0
  
  n = int(fin.readline())
  wn = [float(x) for x in fin.readline().split(' ')]
  wk = [float(x) for x in fin.readline().split(' ')]
  
  wn_asc = sorted(wn)
  wk_asc = sorted(wk)
  wk_max = wk_asc.pop()
  for wn_i in reversed(wn_asc):
    if wn_i > wk_max:
      pts_war += 1
    else:
      if not wk_asc:
        break
      wk_max = wk_asc.pop()
      
  wn_asc = sorted(wn)
  wk_desc = sorted(wk)
  wk_desc.reverse()
  wk_min = wk_desc.pop()
  for wn_i in wn_asc[:-1]:
    if wn_i > wk_min:
      print '%g > %g: wk_desc=%g' % (wn_i, wk_min, wk_desc[-1])
      pts_dwar += 1
      wk_min = wk_desc.pop()
    else:
      print '%g < %g: cancel %g' % (wn_i, wk_min, wk_desc[0])
      del wk_desc[0]
  
  wk_last = wk_min if not wk_desc else wk_desc.pop()
  if wn_asc[-1] > wk_last:
    pts_dwar += 1
  print '\n'
  
  fout.write('Case #%u: %u %u\n' % (i+1,pts_dwar,pts_war))
fin.close()
fout.close()