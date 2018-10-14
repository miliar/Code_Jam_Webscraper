import numpy as np

A_MIN = 1
A_MAX = 2
N_MAX = 10
M_MAX = 10

fin = open('B-large.in')
fout = open('out_large.txt', 'w')

def CanMow(lawn, N, M):
  max_height = lawn.max()
  for cur_height in range(1,max_height+1):
    for i in range(0,N,1):
      for j in range(0,M,1):
        # check if everything in row and column = 1
        if lawn[i,j] == cur_height:
          if not (all(lawn[i,:]==cur_height) or all(lawn[:,j]==cur_height)):
            return(False)
    lawn = np.where(lawn==cur_height,cur_height+1,lawn)
  return(True)

T = int(fin.readline().rstrip('\n'))
for iter in range(T):
  lawn_dims = np.array(fin.readline().rstrip('\n').split(), dtype=int)
  N = lawn_dims[0]
  M = lawn_dims[1]

  # lawn = np.array([], dtype=int)
  lawn = []
  for i in range(0,N,1):
    lawn.append(fin.readline().rstrip('\n').split())

  lawn = np.array(lawn, dtype=int)
  case_num = iter+1
  if CanMow(lawn,N,M):
    fout.write('Case #%d: YES\n' %case_num)
  else:
    fout.write('Case #%d: NO\n' %case_num)
  
fin.close()
fout.close()