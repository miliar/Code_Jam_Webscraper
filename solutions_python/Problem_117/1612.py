import numpy as np

def check_matrix(matrix, value):
   copy_matrix = matrix
   N, M = matrix.shape
   ref_matrix = np.zeros((N, M))
   for i in range(N):
      if matrix[i][0] == value or matrix[i][0] == 0:
         if check_vector_row(matrix, i):
            set_true(ref_matrix, i)

   for i in range(M):
      if matrix[0][i] == value or matrix[0][i] == 0:
         if check_vector_column(matrix, i, ref_matrix):
            set_true_column(ref_matrix, i)

   print matrix, ref_matrix
   if (matrix == value).sum() > (ref_matrix == 1).sum():
      print matrix, (matrix == value).sum(), ref_matrix,(ref_matrix == 1).sum()
      return (matrix, False)

   xs, ys = np.where(ref_matrix == 1)
   for i in range(len(xs)):
      copy_matrix[xs[i]][ys[i]] = 0

   return (copy_matrix, True)
   

def check_vector_row(matrix, i):
   value = matrix[i][0]
   N, M = matrix.shape
   for j in range(M):
      if matrix[i][j] != value and matrix[i][j] != 0.0:
         return False      
   return True

def check_vector_column(matrix, i, ref_matrix):
   value = matrix[0][i]
   N, M = matrix.shape
   for j in range(N):
      if matrix[j][i] != value and matrix[j][i] != 0:
         if ref_matrix[j][i] == 0:
            return False
   return True

def set_true(ref_matrix, i):
   N, M = ref_matrix.shape
   for j in range(M):
      ref_matrix[i][j] = 1

def set_true_column(ref_matrix, i):
   N, M = ref_matrix.shape
   for j in range(N):
      ref_matrix[j][i] = 1

f = open('B-small-attempt1.in', 'r')
g = open('output.txt', 'w')

test_cases = int(f.readline())

for i in range(1, test_cases+1):
   dimensions = map(int, f.readline().split(' '))
   N = dimensions[0]
   M = dimensions[1]
   matrix = np.zeros((N, M))
   for j in range(N):
      matrix[j] = map(int, f.readline().split(' '))

   values = list(set(reduce(list.__add__, matrix.tolist(), [])))

   for value in values:
      matrix, ok = check_matrix(matrix, value)
      if not(ok):
         g.write("Case #" + str(i) + ": NO\n")
         break
   else:
      g.write("Case #" + str(i) + ": YES\n")
