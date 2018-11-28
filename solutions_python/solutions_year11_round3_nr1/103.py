import sys
import functools
def toInt(x):
  return int(x)

def new_matrix(L,C,num):
  return [[num for row in range(C)] for col in range(L)] #@UnusedVariable

file = open('mandar.txt','w')
sys.stdout = file

def check(table,i,j):
  if table[i][j]=='#' and table[i][j+1]=='#' and table[i+1][j]=='#' and table[i+1][j+1]=='#':
    table[i][j]='/' 
    table[i][j+1]='\\' 
    table[i+1][j]='\\' 
    table[i+1][j+1]='/'
    return True
  return False

def checkAll(matrix,N,M):
  for i in range(N):
      for j in range(M):
        if matrix[i][j]=='#':
          return False
  return True

input  = open('a.in')
CASES  = int(input.readline())
for case in range(CASES):
  args = map(toInt,input.readline().strip().split(' '))
  N=args[0]
  M=args[1]
  matrix = []
  for i in range(N):
    line = input.readline().strip()
    matrix.append([c for c in line])
  
  res= ''
  for i in range(N-1):
    for j in range(M-1):
      c = matrix[i][j]
      if c=='#':
        if not check(matrix,i,j):
          res='Impossible'
          break
  
  sys.stdout.write('Case #'+str(case+1)+': \n')
  if checkAll(matrix, N, M):
    res = '' 
  else:
    res = 'Impossible'
  if res:
    sys.stdout.write(res+'\n')
  else:
    for i in range(N):
      for j in range(M):
        sys.stdout.write(matrix[i][j])
      sys.stdout.write('\n')
    
        
      
   
