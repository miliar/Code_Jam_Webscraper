from operator import itemgetter

def parent_small(ac, aj):
  if ac+aj==2:
    acts = []
    acts.append(map(int, raw_input().strip().split(' ')))
    acts.append(map(int, raw_input().strip().split(' ')))
    acts.sort(key=itemgetter(0))
    if ac==2 or aj==2:
      shift = acts[0][1] - acts[0][0] + acts[1][1] - acts[1][0]
      if shift==720:
        if acts[0][1]==acts[1][0] or (acts[0][0]==0 and acts[1][1]==1440):
          return 2
        else:
          return 4
      #blank1 = acts[1][0] - acts[0][1]
      #blank2 = acts[0][0] + 1440 - acts[1][1]
      #if blank1<=720-shift or blank2<=720-shift:
      if (acts[1][1]-acts[0][0])<=720 or (acts[0][1]+1440-acts[1][0])<=720:
        return 2
      else:
        return 4
    else:
      return 2
  raw_input()
  return 2

def parent(ac, aj):
  acts = []
  sum_c = 0
  sum_j = 0
  for i in xrange(ac):
    act = map(int, raw_input().strip().split(' '))
    sum_c += act[1] - act[0]
    act.append('c')
    acts.append(act)
  for i in xrange(aj):
    act = map(int, raw_input().strip().split(' '))
    sum_j += act[1] - act[0]
    act.append('j')
    acts.append(act)
  acts.sort(key=itemgetter(0))
  gaps_c = []
  gaps_j = []
  nblocks_c = ac
  nblocks_j = aj
  for i in xrange(ac+aj-1):
    if acts[i][-1]==acts[i+1][-1]:
      if acts[i][-1]=='c':
        if acts[i+1][0]==acts[i][1]:
          nblocks_c -= 1
        else:
          gaps_c.append(acts[i+1][0] - acts[i][1])
      else:
        if acts[i+1][0]==acts[i][1]:
          nblocks_j -= 1
        else:
          gaps_j.append(acts[i+1][0] - acts[i][1])
  if acts[0][-1]==acts[-1][-1]:
    if acts[0][-1]=='c':
      if acts[-1][1]==1440 and acts[0][0]==0:
        nblocks_c -= 1
      else:
        gaps_c.append(acts[0][0] + 1440 - acts[-1][1])
    else:
      if acts[-1][1]==1440 and acts[0][0]==0:
        nblocks_j -= 1
      else:
        gaps_j.append(acts[0][0] + 1440 - acts[-1][1])
  gaps_c.sort(reverse=True)
  gaps_j.sort(reverse=True)
  stop_c = sum_c==720
  stop_j = sum_j==720
  while not stop_c or not stop_j:
    stop_c = stop_c or len(gaps_c)==0
    stop_j = stop_j or len(gaps_j)==0
    if not stop_c and not stop_j:
      if gaps_c[-1]<gaps_j[-1]:
        gap = gaps_c[-1]
        if sum_c+gap<=720:
          gaps_c.pop()
          sum_c += gap
          nblocks_c -= 1
        else:
          stop_c = True
      else:
        gap = gaps_j[-1]
        if sum_j+gap<=720:
          gaps_j.pop()
          sum_j += gap
          nblocks_j -= 1
        else:
          stop_j = True
    elif not stop_c:
      gap = gaps_c[-1]
      if sum_c+gap<=720:
        gaps_c.pop()
        sum_c += gap
        nblocks_c -=1
      else:
        stop_c = True
    elif not stop_j:
      gap = gaps_j[-1]
      if sum_j+gap<=720:
        gaps_j.pop()
        sum_j += gap
        nblocks_j -=1
      else:
        stop_j = True
  return nblocks_c + nblocks_j + len(gaps_c) + len(gaps_j)

ncases = int(raw_input().strip())
for i in xrange(1, ncases+1):
  ac, aj = map(int, raw_input().strip().split(' '))
  print "Case #%d: %d" % (i, parent(ac, aj))
