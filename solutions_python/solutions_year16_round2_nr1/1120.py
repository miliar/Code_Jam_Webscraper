import sys

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digs = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

def possible(m, dig):
  for ch in dig:
    if m[ch] == 0:
      return False
  return True

def preprocess(m, l):
  for i in range(m['Z']):
    l.append(0)
  m['count'] -= m['Z']*4
  m['E'] -= m['Z']
  m['R'] -= m['Z']
  m['O'] -= m['Z']
  m['Z'] = 0
  for i in range(m['W']):
    l.append(2)
  m['count'] -= m['W']*3
  m['T'] -= m['W']
  m['O'] -= m['W']
  m['W'] = 0
  for i in range(m['U']):
    l.append(4)
  m['count'] -= m['U']*4
  m['F'] -= m['U']
  m['R'] -= m['U']
  m['O'] -= m['U']
  m['U'] = 0
  for i in range(m['X']):
    l.append(6)
  m['count'] -= m['X']*3
  m['S'] -= m['X']
  m['I'] -= m['X']
  m['X'] = 0
  for i in range(m['G']):
    l.append(8)
  m['count'] -= m['G']*5
  m['E'] -= m['G']
  m['I'] -= m['G']
  m['H'] -= m['G']
  m['T'] -= m['G']
  m['G'] = 0

  return l



def solve(m, l):
  if m['count'] == 0:
    return l
  for dig in digs:
    if possible(m, dig):
      l.append(digs.index(dig))
      m['count'] -= len(dig)
      for ch in dig:
        m[ch] -= 1

      ret = solve(m, l)
      if ret == False:
        del l[-1]
        m['count'] += len(dig)
        for ch in dig:
          m[ch] += 1
      else:
        return l
  return False



for tc in range(1, int(input())+1):
  S = input()
  m = {x:0 for x in alpha}
  m['count'] = len(S)
  for c in S:
    m[c] += 1
 # print(m)
  l = preprocess(m, [])
  sys.stdout.flush()
  ret = solve(m, l)
  if ret==False:
    print('\n\nBUG HERE '+S+'\n\n')
  else:
    ret.sort()
    sol = ''.join([str(x) for x in ret])
    print('Case #{_tc}: {_sol}'.format(_tc=tc, _sol=sol))
  sys.stdout.flush()














