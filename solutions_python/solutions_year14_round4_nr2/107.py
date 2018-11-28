from sys import argv
from copy import copy
import itertools

def read_input(f):
  lines = open(f, 'r')
  T = int(lines.readline().strip())


  for i in xrange(T):
    N = int(lines.readline().strip())
    
    A = map(int, lines.readline().strip().split(" "))

    yield i+1, N, A

  lines.close()


def ins_sort_with_count(N, A):
  d = [0] * N
  for i in range(1, N):
        val = A[i]
        j = i - 1
        while (j >= 0) and (A[j] > val):
            A[j+1] = A[j]
            j = j - 1
            d[i] += 1
        A[j+1] = val
  #print A
  return d

def is_valid(A):
  N = len(A)
  i = 0
  while i < N-1 and A[i] < A[i+1]:
    i += 1


  while i < N-1:
    if A[i] < A[i+1]:
      return False
    i += 1 
  return True


def distances(N, A):
  d_ord = ins_sort_with_count(N, A[:])
  d_rev = ins_sort_with_count(N, A[::-1])[::-1]
  print A

  d_ord_sum = [0] * N
  d_rev_sum = [0] * N
  d_ord_sum[0] = d_ord[0]
  d_rev_sum[N-1] = d_rev[N-1]

  for i in xrange(1, N):
    d_ord_sum[i] = d_ord_sum[i-1] + d_ord[i]
  
  min_d = d_ord_sum[N-1]
  
  for i in xrange(N-2, -1, -1):
    d_rev_sum[i] = d_rev_sum[i+1] + d_rev[i]
    d = d_ord_sum[i] + d_rev_sum[i+1]
    if d < min_d:
      min_d = d

  print d_ord_sum
  print d_rev_sum

  return min_d  


def dist(A, B, i=0):
  if i >= len(A):
    return 0

  if A[i] == B[i]:
    return dist(A,B, i+1)
  else:
    j = B.index(A[i])
    assert j-i > 0
    B.pop(j)
    B.insert(i, A[i])
    return abs(i-j) + dist(A, B)


def distances_slow(N, A):
  
  P = filter(is_valid, itertools.permutations(A))
  #best_p = A[:]
  min_d = float('inf')
  for p in P:
    d = dist(A, list(p))
    if d < min_d:
      min_d = d
      #best_p = list(p)

  return min_d#, best_p



if __name__ == '__main__':
  for test_case, N, A in read_input(argv[1]):
    #print " - - - "
    
    res = distances_slow(N, A)   
    #print p  
    print "Case #%d: %s" % (test_case, res)

