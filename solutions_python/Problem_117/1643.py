
import numpy as np

def error(msg=''):
  raise RuntimeError(msg)

def is_possible(table):
  M_max = np.amax(table, axis=0)
  N_max = np.amax(table, axis=1)
  is_max_N_table = np.zeros_like(table, 'bool')
  is_max_M_table = np.zeros_like(table, 'bool')

  for j in xrange(0, N):
    for k in xrange(0, M):
      is_max_N_table[j, k] = table[j, k] == N_max[j]
      is_max_M_table[j, k] = table[j, k] == M_max[k]
      if not (is_max_N_table[j, k] or is_max_M_table[j, k]):
        return False
  return True

f = open('B-large.in')

size = int(f.readline())

for i in xrange(size):
  line = f.readline().split(' ')
  N = int(line[0])
  M = int(line[1])

  table = np.zeros([N, M], 'int')
  for j in xrange(N):
    line = f.readline().split(' ')
    for k in xrange(M):
      table[j, k] = int(line[k])

  print 'Case #%d: '%(i+1),
  if is_possible(table):
    print 'YES'
  else:
    print 'NO'
